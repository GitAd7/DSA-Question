# Brute Force - Make a temp array 
def rot(arr,n):
    temp = [0]*n # Making a new array of same length
    for i in range(1,n):
        temp[i-1] = arr[i]
    temp[n-1] = arr[0]
    for i in range(n):
        print(temp[i], end=" ")
        
arr1 = [1,3,4,5,2]
rot(arr1, len(arr1))
# T.C: O(N) = S.C

# Another Approach- Use temp for storing a single element
def rot_ele(arr,n):
    temp = arr[0] # Storing first element only
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    for i in range(n):
        print(arr[i], end=" ")
        
arr2 = [9,5,6,7,8]
rot_ele(arr2, len(arr2))
# T.C: O(N)
# S.C: O(1) No extra space is used