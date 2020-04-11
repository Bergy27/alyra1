pragma solidity ^0.6.0;

import "github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

contract Credibilite {
  
    using SafeMath for uint256;
  
    mapping (address => uint256) public cred;
    bytes32[] private devoirs;
    
    function produireHash(string memory url) pure public returns(bytes32){
        return keccak256(bytes(url));
    }
    
    
    function transfer(address destinataire, uint256 valeur) private {
        require(cred[msg.sender] > valeur, "Vous n'avez pas assez de \"cred\""); 
        require(cred[destinataire]>0, "Le destinataire doit déjà avoir des \"cred\"");
        require(cred[msg.sender]-valeur >= 1, "Vous devez garder au moins 1 \"cred\"");
        
        cred[destinataire]+=valeur;
        cred[msg.sender]-=valeur;
    }
    
    function remettre(bytes32 dev)  public returns (uint) {
        devoirs.push(dev);
        return devoirs.length;
    }

}