pragma solidity ^0.5.6;
contract Loterie{
    
    uint8 tempsLoterie; //Nombre de jours que la loterie va durer
    uint debutJourLoterie; //Jour x = Début de la loterie
    mapping (uint => uint8) numeroLoteries; //Numéro gagnant par jour (jour => numéro)
    mapping (uint => uint) cagnottes; //Cagnotte par jour (jour => cagnotte)
    mapping (address => mapping(uint => mapping(uint8 => bool))) tickets; //address => jour => numero => joué? Le joueur possède des numéros (éventuels) pour un jour 
    mapping (uint => mapping(uint8 => uint)) numeroJoues; //jour => numero => nombre de fois ou le numéro a été joué (pour le nombre de gagnants)
    mapping (address => bool) dejaRetires; //Verification si le joueur a déjà tenté de retirer ses gains

    constructor() public {
        tempsLoterie = 5;
        debutJourLoterie = jour(block.timestamp);
    }
    

    function jour(uint t) private pure returns (uint) {
        // Indice du jour du moment t
        return t/1 days;
    }
    
    function retirer() public view returns (uint) {
        return cagnottes[0];
    }
    
    /*function retrait() public {
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
    }*/
    

    
    //Possible de tirer au sort si le jour est dépassé (et n'a pas déjà été tiré).
    function numeroGagnant() public returns (uint8) {
        require(jour(block.timestamp)>=debutJourLoterie, "C'est le premier jour du festival");
        require(numeroLoteries[jour(block.timestamp)]==0, "Le numéro a déjà été tiré au sort");
        
        //Numéro gagnant entre 1 et 255 en fonction de la date de la transaction (modulo 255 + 1)
        numeroLoteries[jour(block.timestamp)]=uint8(1+(block.timestamp%255));
        return uint8(1+(block.timestamp%255));
    }
    
    function retirerGains() public {
        require(jour(block.timestamp)>debutJourLoterie+tempsLoterie, "La loterie n'est pas terminé, vous pourrez retirer vos gains à la fin de celle-ci.");
        require(dejaRetires[msg.sender]==false, "Vous avez déjà retiré vos gains.");

        //Parcourir tous les jours de loteries
        for (uint i=debutJourLoterie;i<debutJourLoterie+tempsLoterie;i++) {
            //numeroLoteries[i] ==> numeroGagnant
            //numeroJoues[i][numeroLoteries] ==> nombre de gagnants
            
            //On vérifie si le sender pour le jour i a joué le numéro gagnant (true s'il a joué)
            if (tickets[msg.sender][i][numeroLoteries[i]]) {
                //On divise la cagnotte du jour par le nombre de gagnants
                (msg.sender).transfer(cagnottes[i]/numeroJoues[i][numeroLoteries[i]]);
            }
        }
    }
    
    
    function acheterTicketLoterie(uint8 jours, uint8 numero) public payable {
        require(msg.value==100 finney,"Un ticket coûte 100 Finney.");
        require(jour(block.timestamp)-debutJourLoterie<=jours, "Le délai pour jouer à ce jour est dépassé.");
        require(jours<=tempsLoterie, "Il n'y a pas de ticket à vendre pour cette période.");
        require(numero>=1, "Le numéro choisit doit être plus grand ou égal que 1.");
        require(numero<=255, "Le numéro choisit doit être plus petit ou égal à 255.");
        
        //La cagnotte augmente de 50 finney (Le reste en bénéfice)
        cagnottes[jours]+=50 finney;
        
        //On ajouter 1 au numero joue du jour
        numeroJoues[jours][numero]+=1;
        
        //On met le ticket du jour à true
        tickets[msg.sender][jours][numero] = true;
    }
    
    
    
}