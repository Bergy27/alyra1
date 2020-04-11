pragma solidity ^0.5.6;
contract CagnotteFestival{

    mapping (address => uint) organisateurs;
    mapping (address => bool) estOrganisateur;
    mapping (address => bool) festivaliers;
    uint placesRestantes = 10;
    string[] listSponsors;
    uint256 dateFestival;
    uint256 dateLiquidation;
    uint dateFestivalCurr;
    uint seuilleJour;
    bool premierRetrait;
    uint totalOrganisateurs;
    uint resteOrganisateurs;

    constructor() public {
        estOrganisateur[msg.sender] = true;
        organisateurs[msg.sender] = 100;
        dateFestival = block.timestamp;
        dateLiquidation = dateFestival + 14 days;
        dateFestivalCurr = dateFestival;
        seuilleJour = 1 ether;
        resteOrganisateurs=1;
    }
    
    function retrait() public {
        require(block.timestamp>=dateLiquidation, "Le festival n'est pas terminé");
        require(estOrganisateur[msg.sender], "Vous devez être organisateur.");
        require(organisateurs[msg.sender]>0, "Vous n'avez plus de parts.");
        
        resteOrganisateurs--;
        if (resteOrganisateurs==0) {
            selfdestruct(msg.sender);
        }
        (msg.sender).transfer(address(this).balance*organisateurs[msg.sender]/100);
        organisateurs[msg.sender]=0;
        resteOrganisateurs--;
    }
    
    function fonds(address orga) public view returns (uint) {
        require(estOrganisateur[msg.sender], "Vous devez être organisateur.");
        return organisateurs[orga];
    }
    
    function transfererOrga(address orga, uint parts) public {
        require(estOrganisateur[msg.sender], "Vous devez être organisateur.");
        require(parts<=organisateurs[msg.sender], "Vous n'avez pas suffisamment de part.");
        require(block.timestamp<=dateLiquidation, "Le festival est terminé");
        if (!estOrganisateur[orga]) {
            resteOrganisateurs++;
        }
        estOrganisateur[orga] = true;
        organisateurs[msg.sender]-=(parts);
        organisateurs[orga]+=(parts);
    }
    
    function sponsoriser(string memory nom) public payable {
        require(msg.value>=30 ether,"Le sponsoring coûte au minimum 30 Ethers.");
        listSponsors.push(nom);
    }
    
    function seuilleAtteint(uint256 date, uint montant) internal returns (bool) {
        if (date>=dateFestivalCurr+1 days) {
            dateFestivalCurr=date;
            seuilleJour=1;
        }
        if (seuilleJour>=montant) {
            seuilleJour-=montant;
            return true;
        }
        return false;
    }
    
    function payer(address payable destinataire, uint montant) public {
        require(estOrganisateur[msg.sender], "Vous devez être organisateur.");
        require(destinataire != address(0));
        require(montant > 0);
        //Si la transaction est réalisée sur un nouveau jour, on réinitialise le seuille
        require(seuilleAtteint(block.timestamp, montant), "Le seuille de la journée serait dépassé.");

        destinataire.transfer(montant);
    }
    
    function acheterTicket() public payable {
        require(msg.value>= 500 finney,"Place à 0.5 Ethers");
        require(placesRestantes>0,"Plus de places !");
        festivaliers[msg.sender]=true;
    }
    
    function value() public view returns (uint) {
        return address(this).balance;
    }
}