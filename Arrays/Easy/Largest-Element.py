def largest_element(arr):
    arr.sort()
    return arr[-1]
            
arr1 = [2,5,1,3,0]
print('Largest Element in array is:',largest_element(arr1))
# T.C: O(NlogN)

def larg_ele(arr,n):
    max = arr[0]
    for i in range(0,n):
        if max < arr[i]:
            max = arr[i]
    return max

print('largest Element in array is:', larg_ele(arr1,len(arr1)))
# T.C: O(N)