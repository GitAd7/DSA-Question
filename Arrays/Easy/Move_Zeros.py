# Approach 01 - Brute Force -> Use of Temporary array
def move_zero_end(arr, n):
    temp = [] # Making a Temp array
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i]) # Storing all the Non-Zero element in temp
            
    nz = len(temp) # Lenght of all the Non-Zero Element
    
    for i in range(nz): # Replacing the element of main arr with temp array
        arr[i] = temp[i]
        
    for i in range(nz,n): # Filling remaining spaces with 0
        arr[i] = 0
    return arr

arr1 = [1,0,2,0,4,3,0,1]
move_zero_end(arr1, len(arr1))
print(arr1)
# T.C: O(2*N)
# S.C: O(N) For making a array of same size as N

# Approach 02 - Optimized -> Utilising the two-pointers for swaping elements till 0's reach to last
def move_zero_opt(arr, n):
    j = -1
    for i in arr:
        if arr[i] == 0:
            j = i
            break
    if j == -1:
        return arr
    for i in range(j+1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

arr2 = [1,2,0,4,0,1,0]
move_zero_opt(arr2, len(arr2))
print(arr2)