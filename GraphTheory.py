# Liste appelé sommet

sommet = ['A','B','C','D']
graphe = [[0,3,0,7],[0,2,0,5],[0,2,0,2],[0,2,9,0]]

# Fonction qui retourne la liste des arêtes triées par ordre croissant à partir de la matrice d'adjacence...

def trier_aretes(graphe):
    aretes = []
    for i in range(len(graphe)):
        for j in range(len(graphe[i])):
            poids = graphe[i][j]
            if poids != 0:
                arrete = (sommet[i], sommet[j], poids)
                aretes.append(arrete)
    aretes_triees = sorted(aretes, key=lambda x: x[2])
    return aretes_triees

print('fonction 1 :',trier_aretes(graphe))


# Fonction adjacent (graphe, noeud1, noeud2) qui retourne vrai ou faux pour savoir si les 2 noeuds sont adjacents

def adjacent(graphe, noeud1, noeud2):
    if graphe[sommet.index(noeud1)][sommet.index(noeud2)] != 0:
        return True
    else:
        return False

print('fonction 2 :',adjacent(graphe, 'A', 'C'))


# Fonction Kruskall qui retourne la liste des arêtes qui constituent l'arbre couvrant minimum

def kruskall(graphe):
    aretes = trier_aretes(graphe)
    arbre = []
    for arrete in aretes:
        if arrete[0] not in arbre and arrete[1] not in arbre:
            arbre.append(arrete[0])
            arbre.append(arrete[1])
    return arbre

print('fonction 3 :',kruskall(graphe))

# La fonction appartient(listeArête, noeud) qui retourne vrai ou faux si le noeud appartient à la liste d'arêtes

