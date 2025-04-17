def insertion_sort(arr, i, n):
    if i == n: # Base Case
        return
    while i>0 and arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        i -= 1
    insertion_sort(arr, i+1, n)# Calling function again
    
arr1 = [2,5,6,7,4,8,1]
insertion_sort(arr1, 0, len(arr1))
print(arr1)