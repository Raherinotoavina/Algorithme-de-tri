# Tri par fusion ou tri dichotomique
# Si le tableau n'a qu'un élément, il est déjà trié.
# Sinon, séparer le tableau en deux parties à peu près égales.
# Trier récursivement les deux parties avec l'algorithme du tri fusion.
# Fusionner les deux tableaux triés en un seul tableau trié.
def fusion(gauche,droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):        
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat

def diviser(arr) :
    if (len(arr) <= 1) :
        return arr
    milieu = len(arr)//2
    gauche = arr[:milieu]
    droite = arr[milieu:]
    gauche = diviser(arr[:milieu])
    droite = diviser(arr[milieu:])
    return list(fusion(gauche,droite))

print(diviser([1,2,4,5,1,2,3,5,1,2,5,4,1,2]))