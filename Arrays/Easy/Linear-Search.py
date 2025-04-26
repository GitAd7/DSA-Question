# Searching for an element in a array
def linear_search(arr, k:int):
    n = len(arr)
    for i in range(n):
        if arr[i] == k:
            return i
    return -1

arr1 = [1,2,3,4,5,6,7]
ind = linear_search(arr1, 0)
print(ind)