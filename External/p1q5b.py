def binary_search(arr, low, high, find_x):

    if high > low:

        mid = (low + high) // 2

        if arr[mid] == find_x:
            return mid
        elif arr[mid] < find_x:
            return binary_search(arr, mid +1, high, find_x)
        else:
            return binary_search(arr, low, mid -1, find_x)
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 4
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
    
