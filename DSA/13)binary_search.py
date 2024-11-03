def binary_search(arr, low, high, x): 
    if high >= low: 
        mid = (high + low) // 2 
        # Check if the middle element is the target
        if arr[mid] == x: 
            return mid 
        # If the target is smaller, search in the left half
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
        # If the target is larger, search in the right half
        else: 
            return binary_search(arr, mid + 1, high, x) 
    else: 
        return -1 

arr = [2, 3, 4, 10, 40] 
x = 10 
result = binary_search(arr, 0, len(arr) - 1, x) 

if result != -1: 
    print("Element is present at index", result) 
else: 
    print("Element is not present in array")
