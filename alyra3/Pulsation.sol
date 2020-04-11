pragma solidity ^0.5.7;
contract Pulsation {

    uint public battement;
    string private message;

    constructor(string memory _message) public {
        message=_message;
        battement=0;
    }

    function ajouterBattement() public returns(string memory) {
        battement++;
        if (block.number%10==0) {
            return "Criii";
        }
        return message;
    }
}

contract Pendule {

    string[] public balancier;
    Pulsation contratTac;
    Pulsation contratTic;
    
    constructor() public {
        contratTic = new Pulsation("tic");
        contratTac = new Pulsation("tac");
    }
    
    function compareStrings (string memory a, string memory b) private pure returns (bool) {
        return (keccak256(abi.encodePacked((a))) == keccak256(abi.encodePacked((b))) );
    }
    
    function inspection() public view returns(int) {
        int indexError = -1;
        for (uint i=0;i<balancier.length;i++) {
            if (compareStrings(balancier[i],"Criii")) {
                return int(i);
            }
        }
        return indexError;
    }

    function mouvementsBalancier(uint k) public {
        while (k>0) {
            balancier.push(contratTic.ajouterBattement());
            balancier.push(contratTac.ajouterBattement());
            k--;
        }
    }
}