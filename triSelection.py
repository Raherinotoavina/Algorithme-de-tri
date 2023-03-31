# Sur un tableau de n éléments (numérotés de 0 à n-1 , attention un tableau de 5 valeurs (5 cases) 
# sera numéroté de 0 à 4 et non de 1 à 5), le principe du tri par sélection est le suivant :
# rechercher le plus petit élément du tableau, et l'échanger avec l'élément d'indice 0 ;
# rechercher le second plus petit élément du tableau, et l'échanger avec l'élément d'indice 1 ;
# continuer de cette façon jusqu'à ce que le tableau soit entièrement trié.

def triSelection(arr) :
    for i in range (0, len(arr)) :
        min, a = arr[i], i
        for j in range(i+1, len(arr)) :
            if min > arr[j] :
                min,a=arr[j],j
        arr[a],arr[i]=arr[i],arr[a]
        
    return(arr)

print(triSelection([4,1,3,5,1,2,75,1,5,46,4,9]))