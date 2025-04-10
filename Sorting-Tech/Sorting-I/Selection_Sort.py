def selection_sort(arr,n):
    for i in range(0,n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
# Pythonic way of doing swap
        arr[i], arr[mini] = arr[mini],arr[i]
# One way to do swapping
'''        temp = 0 
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp'''

arr1 = [3,5,6,8,2,7]
selection_sort(arr1,6)
print(arr1)