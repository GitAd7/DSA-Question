def bubble_sort(arr, n):
    if n==1: # Base case for recursion
        return
    for j in range(0,n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
    bubble_sort(arr, n-1) # Caliing recursive function after reduction

arr1 = [2,5,6,7,4,8,1]
bubble_sort(arr1, len(arr1))
print(arr1)
# Same optimization method can be used as i have utilized with iterative bubble sort