def insertion_sort(arr,n):
    for i in range(0,n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -= 1

arr1 = [2,6,8,9,3,29,1,34,65,67,89]
insertion_sort(arr1, len(arr1))
print(arr1)
# Worst/Average T.C: O(n^2) for unordered array
# Best T.C: O(n) for ordered array