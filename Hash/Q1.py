# Counting Distinct Element
def CountElement(arr):
    dis_count = {}
    for i in range(len(arr)):
        if arr[i] not in dis_count:
            dis_count[arr[i]] = i
    return len(dis_count)

arr = [1,2,1,3,4,5,2,3,6]
print("Number of Distinct Element in an array is:", CountElement(arr))

arr1 = [15,12,13,12,12,13,18]
print("Number of Distinct Element in an array is:", CountElement(arr1))

arr2 = [10,10,10]
print("Number of Distinct Element in an array is:", CountElement(arr2))