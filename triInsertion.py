# Pour trouver la place où insérer un élément parmi les précédents,
# il faut le comparer à ces derniers, et les décaler afin de libérer
# une place où effectuer l'insertion. Le décalage occupe la place laissée libre
# par l'élément considéré. En pratique, ces deux actions s'effectuent en une passe,
# qui consiste à faire « remonter » l'élément au fur et à mesure jusqu'à rencontrer un élément plus petit.

def triInsertion(arr) :
    for i in range(0, len(arr)):
        for j in range(0,i+1) :
            if (i+1 > 1 and arr[i] < arr[j]) :
                arr[j],arr[i] = arr[i],arr[j]
    return arr

print(triInsertion([4,1,2,35,4,7]))