//Write your own contracts here. Currently compiles using solc v0.4.15+commit.bbb8e64f.
pragma solidity ^0.4.25;
contract SceneOuverte {

    string[12] passagesArtistes;
    uint creneauxLibres = 12;
    //entiers sont automatiquement initialisés à “0”
    uint tour;

    function sInscrire(string nomDArtiste) public { 
        if (creneauxLibres>0) {
            passagesArtistes[12-creneauxLibres] = nomDArtiste;
            creneauxLibres--;
        }
    }

    function passerArtisteSuivant() public {
        bytes memory tempEmptyStringTest = bytes(passagesArtistes[tour+1]);
        if (tempEmptyStringTest.length != 0 && tour+1<12) {
            tour += 1;
        }
    }

    function artisteEnCours () public constant returns (string) {
        if (tour+1<=11) { 
          bytes memory tempEmptyStringTest = bytes(passagesArtistes[tour+1]);
          if (tempEmptyStringTest.length == 0 || tour==11) {
              return string(abi.encodePacked(passagesArtistes[tour], ". FIN, c'est le dernier artiste"));
          } else {
              return passagesArtistes[tour];
          }
        }
        return string(abi.encodePacked(passagesArtistes[tour], ". FIN, c'est le dernier artiste"));
    }
}