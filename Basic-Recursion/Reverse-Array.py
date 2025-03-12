# Iterative Approach 1
arr = [1,2,3,4]
rev_arr = []
n = len(arr)
for i in range(n):
    rev_arr.append(arr[n-1-i])
print(rev_arr)

# Iterative Approach 2: Modifying the same array
arr[:] = arr[::-1]

# Through Recursion
def ReverseArray(array, left=0, right=None):
    right = len(array)-1
    
    # base case
    if left >= right:
        return
    
    array[left], array[right] = array[right], array[left]
    return ReverseArray(array, left+1, right-1)
    