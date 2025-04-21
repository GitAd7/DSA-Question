# We can use similar methods where wether we can make a temp array, or we can use the same array
# Since both the methids have already been implemented before, we will go thrpugh the optimized one

# Making a reversal algo
def reversal(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
# Now make function for roation for left 
def rotateleft(arr, n, k):
    # first k elements
    reversal(arr, 0, k-1)
    # remaining n-k element
    reversal(arr, k, n-1)
    # whole array
    reversal(arr, 0, n-1)
    
# Make a function for rotation to right
def rotateright(arr,n,k):
    # first n-k elements
    reversal(arr, 0, n-k-1)
    # remaining elements
    reversal(arr, n-k, n-1)
    # Whole array
    reversal(arr, 0, n-1)
    
arr1 = [1,2,3,4,5,6,7,8]
k = 3

# Rotate left
arr_left = arr1.copy()
rotateleft(arr_left, len(arr_left), k)
print(f"Array after rotating {k} places to the left: {arr_left}")

# Rotate right
arr_right = arr1.copy()
rotateright(arr_right, len(arr_right), k)
print(f"Array after rotating {k} places to the right: {arr_right}")