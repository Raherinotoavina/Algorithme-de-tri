import random
# La méthode consiste à placer un élément du tableau (appelé pivot)
# à sa place définitive, en permutant tous les éléments de telle sorte que
# tous ceux qui sont inférieurs au pivot soient à sa gauche et que
# tous ceux qui sont supérieurs au pivot soient à sa droite.  

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot, left, right = arr[0], [], []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quicksort(left) + [pivot] + quicksort(right)

listes = [random.randint(0, 50) for x in range(60)]

print(quicksort(listes))