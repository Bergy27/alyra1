pragma solidity ^0.5.7;
contract Assemblee {
    string public nomAssemblee;
    
    mapping (address => bool) administrateurs;
    mapping (address => bool) membres;
    mapping (address => uint) blames;
    struct Decision {
        string description;
        uint votesPour;
        uint votesContre;
        mapping (address => bool) aVote;
        bool status;
    }
    Decision[] decisions;

    constructor(string memory nom) public {
        nomAssemblee=nom;
        membres[msg.sender]=true;
        administrateurs[msg.sender]=true;
    }
    
    function nommerAdministrateurs(address utilisateur) public {
        require(administrateurs[msg.sender], "Vous n'êtes pas administrateur.");
        require(membres[utilisateur], "L'utilisateur doit être membre.");
        administrateurs[utilisateur] = true;
    }
    
    function demissionner() public {
        require(administrateurs[msg.sender], "Vous n'êtes pas administrateur.");
        administrateurs[msg.sender]=false;
    }

    function rejoindre() public {
        require(membres[msg.sender]==false, "Vous êtes déjà membre.");
        require(blames[msg.sender]<2, "Vous avez été banni.");
        membres[msg.sender]=true;
    }
    
    function fermeDecision(uint indice) public {
        require(administrateurs[msg.sender], "Vous n'êtes pas administrateur.");
        require(indice+1<=decisions.length, "La décision n'existe pas.");
        decisions[indice].status = false;
    }
    
    function blamer(address utilisateur) public {
        require(administrateurs[msg.sender], "Vous n'êtes pas administrateur.");
        require(membres[utilisateur], "L'utilisateur doit être membre.");
        blames[utilisateur]++;
        if (blames[utilisateur]>=2) {
            membres[utilisateur]=false;
        }
    }

    function proposerDecision(string memory description) public {
        require(membres[msg.sender], "Il faut être membre!");
        Decision memory decision = Decision({
            description : description,
            votesPour : 0,
            votesContre : 0,
            status : true
        });
        decisions.push(decision);
    }

    function voter(uint indice, bool value) public {
        require(membres[msg.sender], "Il faut être membre!");
        require(indice+1<=decisions.length, "La décision n'existe pas.");
        require(decisions[indice].status, "La votation est fermée.");
        require(decisions[indice].aVote[msg.sender]==false, "L'utilisateur a déjà voté pour cette décision");
        if (value) {
            decisions[indice].votesPour++;
        } else {
            decisions[indice].votesContre++;
        }
        decisions[indice].aVote[msg.sender] = true;
    }
    
    function comptabiliser(uint indice) public view returns (int){
        require(indice+1<=decisions.length, "La décision n'existe pas.");
        return int(decisions[indice].votesPour-decisions[indice].votesContre);
    }
}