def bubble_sort(arr,n):
    for i in range(n,1,-1):
        for j in range(0,i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr1 = [2,5,6,7,4,8,1]
bubble_sort(arr1, len(arr1))
print(arr1) # T.C: O(n^2)

def opt_bubble_sort(arr,n):
    for i in range(n,1,-1):
        didswap = 0
        for j in range(0,i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                didswap = 1
        if didswap == 0:
            break

arr2 = [1,2,3,4,5,6]
opt_bubble_sort(arr2, len(arr2))
print(arr2) # T.C: O(n) for the case when array is already in sorted manner