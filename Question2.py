from itertools import combinations

def findPairs(arr, k):
    return[(x,y) for x,y in combinations(arr, r=2)
            if abs(x-y) == k]

_list = [1,3,5]
k = 2

Pairs = findPairs(_list, k)
print("Pairs with difference {0} are {1}".format(k, Pairs))