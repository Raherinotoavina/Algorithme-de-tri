# Le tri à bulles ou tri par propagation1 est un algorithme de tri.
# Il consiste à comparer répétitivement les éléments consécutifs d'un tableau,
# et à les permuter lorsqu'ils sont mal triés. Il doit son nom au fait qu'il déplace
# rapidement les plus grands éléments en fin de tableau, comme des bulles d'air qui
# remonteraient rapidement à la surface d'un liquide.

def triABulle (arr) :
    for i in range (0, len(arr)) :
        for j in range(i, len(arr)) :
            if arr[i] > arr[j] :
                arr[i], arr[j] = arr[j], arr[i]
    return(arr)

print(triABulle([1,4,2,1,4,75,3,2,5]))