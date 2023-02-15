class ABR:
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite
    
    def get_racine(self):
        return self.racine
    
    def set_racine(self, racine):
        self.racine = racine
    
    def get_gauche(self):
        return self.gauche
    
    def set_gauche(self, gauche):
        self.gauche = gauche
    
    def get_droite(self):
        return self.droite
    
    def set_droite(self, droite):
        self.droite = droite
    
    def estVide(self):
        return self.racine is None
    
    def prefixe(self):
        if self.estVide():
            return []
        else:
            res = [self.racine]
            if self.gauche is not None:
                res += self.gauche.prefixe()
            if self.droite is not None:
                res += self.droite.prefixe()
            return res
    
    def infixe(self):
        if self.estVide():
            return []
        else:
            res = []
            if self.gauche is not None:
                res += self.gauche.infixe()
            res += [self.racine]
            if self.droite is not None:
                res += self.droite.infixe()
            return res
    
    def postfixe(self):
        if self.estVide():
            return []
        else:
            res = []
            if self.gauche is not None:
                res += self.gauche.postfixe()
            if self.droite is not None:
                res += self.droite.postfixe()
            res += [self.racine]
            return res
    
    def taille(self):
        if self.estVide():
            return 0
        else:
            return 1 + (self.gauche.taille() if self.gauche is not None else 0) + (self.droite.taille() if self.droite is not None else 0)
    
    def hauteur(self):
        if self.estVide():
            return -1
        else:
            return 1 + max((self.gauche.hauteur() if self.gauche is not None else -1), (self.droite.hauteur() if self.droite is not None else -1))
# créer un arbre binaire de recherche de taille 25 et de hauteur 5
arbre = ABR(50, ABR(25, ABR(10, ABR(5), ABR(15)), ABR(35, ABR(30), ABR(40, ABR(37), ABR(45, ABR(42), ABR(48))))), ABR(75, ABR(60, ABR(55), ABR(65, ABR(63), ABR(70))), ABR(90, ABR(85, ABR(80), ABR(87)), ABR(100, ABR(95), ABR(110, ABR(105), ABR(120))))))


# afficher la racine de l'arbre
print("La racine de l'arbre est : ", arbre.get_racine())

# afficher les sous-arbres gauche et droit de la racine
print("Le sous-arbre gauche de la racine est : ", arbre.get_gauche().get_racine())
print("Le sous-arbre droit de la racine est : ", arbre.get_droite().get_racine())

# afficher les parcours préfixe, infixe et postfixe de l'arbre
print("Le parcours préfixe de l'arbre est : ", arbre.prefixe())
print("Le parcours infixe de l'arbre est : ", arbre.infixe())
print("Le parcours postfixe de l'arbre est : ", arbre.postfixe())

# afficher la taille et la hauteur de l'arbre
print("La taille de l'arbre est : ", arbre.taille())
print("La hauteur de l'arbre est : ", arbre.hauteur())