def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1
    while(left <= mid and right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high+1):
        arr[i] = temp[i-low]


def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low+high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

arr1 = [3,1,2,4,1,5,6,2,4]
merge_sort(arr1, 0, len(arr1)-1)
print(arr1)