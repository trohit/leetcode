
def get_permutations(arr):
  
    def swap(arr, i, j):
        print(f"{i}<>{j}")
        (arr[i], arr[j]) = (arr[j], arr[i])
    
    def helper(a, i, res, lvl = 0):
        print(f"{' ' *lvl*2}lvl:{lvl} i:{i} a:{a}")
        # base case / leaf node
        if i == len(a) - 1:
            print(f"{' ' *lvl*2}appending a:{a}")
            res.append(a.copy())
            return
        
        # intermediate / nested node
        # print(f"{' ' *lvl*2}ph1 sl:{sl} a:{a}")
        for j in range(i, len(arr)):
            swap(a, i, j)
            helper(a, i+1, res, lvl+1)
            swap(a, i, j)

    res = []
    helper(arr, 0, res)
    return res
