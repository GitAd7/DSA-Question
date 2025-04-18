def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while i<j:
        while arr[i] <= pivot and i<= high: # Check-01
            i += 1
        while arr[j] > pivot and j >= low+1:# Check-02
            j -= 1
        if i < j:
            arr[i], arr[j] =  arr[j], arr[i] # Swap values
    arr[low] , arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low>=high:
        return
    pindex = partition(arr, low, high)
    quick_sort(arr, low, pindex-1) # left subarray
    quick_sort(arr, pindex+1, high) # right subarray
    
arr1 = [2,5,6,7,4,8,1]
quick_sort(arr1, 0, len(arr1)-1)
print(arr1)

# Best/Average T.C: O(NlogN) when the pivot is selected as mid element or near middle element
# Worst T.C: O(N^2) when the pivot is selected as smallest or greatest element