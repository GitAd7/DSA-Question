# Approach-01 Brute Force
# Assumption: The array does not have any duplicates value
def find_ele(arr, n):
    if n==1: # Edge Case
        return -1
    arr.sort()
    sec_sml = arr[1]
    sec_lar = arr[-2]
    return sec_sml, sec_lar

arr1 = [3,4,8,2,1,90,142]
print('Second smalles and largest element in array are:', find_ele(arr1, len(arr1)))
# T.C: O(NlogN) for sorting the array
# This approach is not fit mainly due to the assumption we have taken
# A better approach must be implemented which would be faster to implement and can paas through the assumption



# Approach-02
# Store the smalles and largest and then check for the second smalles and largest element in array
def ele_hunt(arr, n):
    if n == 0 or n==1: # Edge Cases
        return -1
    small = float('inf')
    sec_sml = float('inf')
    large = float('-inf')
    sec_lrg = float('-inf')
    for i in range(n): # First store the smallest and largest element present 
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < sec_sml and arr[i] != small:
            sec_sml = arr[i]
        if arr[i] > sec_lrg and arr[i] != large:
            sec_lrg = arr[i]
    
    print('Second Smalles element in array:', sec_sml)
    print('Second Largest Element in array:', sec_lrg)
    
arr2=[1,2,4,6,7,5,3,2,7,8,2,1,9,2,5,7]
ele_hunt(arr2, len(arr2))
# T.C: O(N)
# Here we are traversing array two times although the complexity is O(N) 
# We need to find a way to traverse array for one time only.


# Approach - 03
# Making different functions for small and large
def sec_sml(arr, n):
    if n < 2:
        return -1
    small = float('inf')
    ss = float('inf')
    for i in range(n):
        if arr[i] < small:
            ss = small
            small = arr[i]
        if arr[i] < ss and arr[i] != small:
            ss = arr[i]
    return ss

def sec_lar(arr,n):
    if n<2:
        return -1
    large = float('-inf')
    sl = float('-inf')
    for i in range(n):
        if arr[i] > large:
            sl = large
            large = arr[i]
        if arr[i] > sl and arr[i] != large:
            sl = arr[i]
    return sl

arr3 = [1, 2, 4, 7, 7, 5] 
print('Second Smalled element:', sec_sml(arr3, len(arr3)))
print('Second Largest element:', sec_lar(arr3, len(arr3)))
# T.C: O(N) Single Traversal
# This is the most optimal solution among all the others