# Optimized Approach Two Pointer
def rem(arr, n):
    if n == 0:
        return 
    arr.sort()
    i = 0
    for j in range(1,n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i+1

arr1 = [1,2,3,1,4,6,7,3,2,1,1]
print(rem(arr1, len(arr1)))
k = rem(arr1, len(arr1))
for i in range(k):
    print(arr1[i], end=" ")