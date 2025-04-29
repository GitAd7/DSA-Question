# The task is to take a union of two sorted arrays in ascending order.

# Approach 01 - Using Hashmap
def union_map(arr1, arr2):
    count = {} # Making a dictionary
    for i in range(len(arr1)): # Storing element frequency of arr1
        if arr1[i] not in count:
            count[arr1[i]] = i
            
    for j in range(len(arr2)): # Saving frequency element of arr2 if not in arr1
        if arr2[j] not in count:
            count[arr2[j]] = j
            
    return list(count.keys()) # Getting only the keys of the dictionary

arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
print(union_map(arr1,arr2))
# T.C: O(m+n)
# S.C: O(m+n)

# Appraoch 02 - Using Set
def union_set(arr1, arr2):
    s = set()
    union = []
    
    for nums in arr1:
        s.add(nums) # Add elements of arr1 in set
        
    for nums in arr2:
        s.add(nums) # Add elements of arr2 in set
        
    for nums in s:
        union.append(nums) # Add all the set elements in a new array
        
    return union

arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
print(union_set(arr1,arr2))
# T.C: O(m+nlog(m+n))
# S.C: O(m+n)