class Noeud:
    def __init__(self, v, parent=None):
        self.valeur = v
        self.parent = parent
        self.gauche = None
        self.droite = None
    
    #Affiche la valeur du noeud et la valeur de ses deux enfants et de son parent    
    def toString(self):
        out = "Noeud " + str(self.valeur) + ":  L";
        if(self.gauche is None):
            out += "-"
        else: 
            out += str(self.gauche.valeur)
        out += " R";
        if(self.droite is None):
            out += "-"
        else:
            out += str(self.droite.valeur)
        out += " P";
        if(self.parent is None):
            out += "-"
        else:
            out += str(self.parent.valeur)
        
        print(out)


class Arbre:
    def __init__(self):
        self.racine = None

    #Méthode pour ajouter un noeud    
    def ajouterNoeud(self, val):
        if self.racine is None:
            self.racine = Noeud(val)
        else:
            self._ajouterNoeud(val, self.racine)

    def _ajouterNoeud(self, val, noeud_courrant):
        if val<noeud_courrant.valeur:
            if noeud_courrant.gauche is None:
                noeud_courrant.gauche = Noeud(val, noeud_courrant)
            else:
                self._ajouterNoeud(val, noeud_courrant.gauche)
        else:
            if noeud_courrant.droite is None:
                noeud_courrant.droite = Noeud(val, noeud_courrant)
            else:
                self._ajouterNoeud(val, noeud_courrant.droite)

    #Méthode pour trouver une valeur donnée dans un arbre binaire de recherche
    def trouverNoeud(self, val):
        if self.racine.valeur==val:
            return self.racine
        else:
            return self._trouverNoeud(val, self.racine)

    def _trouverNoeud(self, val, noeud_courrant):
        if noeud_courrant is None:
            return None
        if noeud_courrant.valeur==val:
            return noeud_courrant
        elif val<noeud_courrant.valeur:
            return self._trouverNoeud(val, noeud_courrant.gauche)
        else:
            return self._trouverNoeud(val, noeud_courrant.droite)

    def noeudEstFeuille(self, val):
        noeud = self.trouverNoeud(val)
        if noeud is None:
            return False
        if noeud.gauche is None and noeud.droite is None:
            return True
        else:
            return False

    #Méthode pour supprimer un noeud
    def supprimerNoeud(self, val):
        noeudToDelete = self.trouverNoeud(val)
        if self.noeudEstFeuille(noeudToDelete.valeur):
            print("feuille")
            if noeudToDelete.valeur>noeudToDelete.parent.valeur:
                noeudToDelete.parent.droite = None
            else:
                noeudToDelete.parent.gauche = None
            noeudToDelete.parent = None
        
        elif noeudToDelete.gauche is not None and noeudToDelete.droite is not None:
            sous_arbre = noeudToDelete.gauche
            while not self.noeudEstFeuille(sous_arbre.valeur):
                if sous_arbre.droite is None:
                    sous_arbre = sous_arbre.gauche
                else:
                    sous_arbre = sous_arbre.droite

            if noeudToDelete.valeur>noeudToDelete.parent.valeur:
                noeudToDelete.parent.droite = sous_arbre
            else:
                noeudToDelete.parent.gauche = sous_arbre
            if sous_arbre.valeur>sous_arbre.parent.valeur:
                sous_arbre.parent.droite = None
            else:
                sous_arbre.parent.gauche = None
            sous_arbre.parent = noeudToDelete.parent
            sous_arbre.gauche = noeudToDelete.gauche
            sous_arbre.droite = noeudToDelete.droite
            noeudToDelete.parent = None
            noeudToDelete.gauche = None
            noeudToDelete.droite = None


        elif noeudToDelete.gauche is not None:
            noeudToDelete.gauche.parent = noeudToDelete.parent
            if noeudToDelete.valeur>noeudToDelete.parent.valeur:
                noeudToDelete.parent.droite = noeudToDelete.gauche
            else:
                noeudToDelete.parent.gauche = noeudToDelete.gauche
            noeudToDelete.gauche = None
            noeudToDelete.droite = None
            noeudToDelete.parent = None
        elif noeudToDelete.droite is not None:
            noeudToDelete.droite.parent = noeudToDelete.parent
            if noeudToDelete.valeur>noeudToDelete.parent.valeur:
                noeudToDelete.parent.droite = noeudToDelete.droite
            else:
                noeudToDelete.parent.gauche = noeudToDelete.droite
            noeudToDelete.gauche = None
            noeudToDelete.droite = None
            noeudToDelete.parent = None
            
        
    #Méthode pour afficher l’arbre selon un parcours infixe
    #Cette méthode doit retournée un tableau contenant la valeur des noeuds        
    def infixe(self):
        if self.noeudEstFeuille(self.racine.valeur):
            return [self.racine.valeur]
        elif self.racine.gauche is not None:
            return self._infixe(self.racine.gauche, [])
        else:
            return self._infixe(self.racine.droite, [])



    def _infixe(self, noeud, out):
        #self.printNoeud(noeud.valeur)
        if noeud.valeur in out:
            if noeud.parent is None:
                return list(map(lambda element : str(element), out))
            else:
                if noeud.droite is not None:
                    return self._infixe(noeud.parent, out)
                else:
                    return list(map(lambda element : str(element), out))
        if self.noeudEstFeuille(noeud.valeur):
            out.append(noeud.valeur)
            return self._infixe(noeud.parent, out)
        if noeud.gauche is not None and noeud.gauche.valeur not in out:
            return self._infixe(noeud.gauche, out)
        elif noeud.gauche is not None and noeud.gauche.valeur in out:
            if noeud.droite is not None and noeud.droite.valeur not in out:
                out.append(noeud.valeur)
                return self._infixe(noeud.droite, out)
            elif noeud.droite is not None and noeud.droite.valeur in out:
                return self._infixe(noeud.parent, out)
            elif noeud.droite is None:
                out.append(noeud.valeur)
                return self._infixe(noeud.parent, out)
        elif noeud.gauche is None:
            if noeud.droite.valeur not in out:
                out.append(noeud.valeur)
                return self._infixe(noeud.droite, out)
            else:
                return self._infixe(noeud.parent, out)
        
    #Méthode pour afficher la valeur d'un noeud à partir de sa valeur        
    def printNoeud(self, val):
        noeud = self.trouverNoeud(val)

        if noeud is not None:
            noeud.toString();
        else:
            print("ERROR")


a = Arbre()
a.ajouterNoeud(30)
a.ajouterNoeud(18)
a.ajouterNoeud(24)
a.ajouterNoeud(11)
a.ajouterNoeud(33)
a.ajouterNoeud(13)
a.ajouterNoeud(40)
a.ajouterNoeud(46)
a.ajouterNoeud(14)
a.ajouterNoeud(21)
a.ajouterNoeud(12)
a.ajouterNoeud(10)
a.ajouterNoeud(31)
a.ajouterNoeud(35)
a.ajouterNoeud(32)

print(a.infixe())

#['10', '11', '12', '13', '14', '18', '21', '24', '30', '31', '32', '33', '35', '40', '46']
#[10, 11, 12, 13, 14, 18, 21, 24, 30, 31, 32, 33, 35, 40, 46]


#['10', '11', '12', '13', '14', '18', '21', '30', '31', '32', '33', '35', '40', '46']

