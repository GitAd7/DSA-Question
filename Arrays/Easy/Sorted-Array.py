# To check if array is sorted or not

# Approach-01 Brute Force - Double Indexing
def is_sorted(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                return True
    return False

arr1 = [1,2,3,4,5]
print(is_sorted(arr1, len(arr1)))
# T.C: O(N^2) traversing array twice

# Approach-02 Optimized - Single Traversal
def issorted(arr, n):
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True

arr2 = [5,1,2,3,4]
print(issorted(arr2, len(arr2)))
# T.C: O(N)