
def binary_search_rec(arr, left, right, target):
    # If the arr range is invalid
    if left > right:
        return -1
        
    mid = (left + right)//2
    
    if arr[mid] == target:
        return mid
        
        # If the target value is smaller than mid value
    if arr[mid] > target:
        return binary_search_rec(arr, left, mid - 1, target)
    else:
        return binary_search_rec(arr, mid + 1, right, target)
    
    
# Driver code to test the function
if __name__ == "__main__":
    arr = [2,4,6,8,10,12,14,16]
    
    target = int(input("Enter the target value: "))
    
    result = binary_search_rec(arr, 0, len(arr) - 1, target)
    
    if result != -1:
        print(f"The target value is found {result}")
    else:
        print(f"Target value is not found at {result}")

# Time Complexity:
| Case             | Description                                                 | Time Complexity |
| ---------------- | ----------------------------------------------------------- | --------------- |
| **Best Case**    | Element found at the first middle check                     | **O(1)**        |
| **Average Case** | Element found somewhere in middle after log₂(n) divisions   | **O(log n)**    |
| **Worst Case**   | Element not found, algorithm checks until subarray size = 1 | **O(log n)**    |

        
