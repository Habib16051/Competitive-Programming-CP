def merge_sort(arr):
    # if the array length is 0 or 1, the the array is already sorted
    if len(arr) <= 1:
        return arr
    # Find the the middle value of the array
    mid = len(arr)//2

    # Divide the array into two half
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Sorting the each half array
    left_sorted_arr = merge_sort(left_half)
    right_sorted_arr = merge_sort(right_half)

    # Finally merge the both half into together
    return merge(left_sorted_arr, right_sorted_arr)

# This is the method that combine the final two merged half together and finally merge the whole array
def merge(left, right):
    # Take the initaial result is empty
    result = []
    # Initialize the i and j is 0
    i = j = 0

    while i < len(left) and j < len(right):
        # if the left is samller than or equal to right value
        # then add the ith value to the result array and increased by 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        # Otherwise add the right value
        # increase it by 1
            
        else:
            result.append(right[j])
            j += 1
    # Added the remaining value in each side (Specially for the last single value for each half)
    result.extend(left[i:])
    result.extend(right[j:])
    # return the final result
    return result
    
    
if __name__ == "__main__":
    arr = [10, 3,100, 55,32,27, 12,36]
    
    sorted_array = merge_sort(arr)
    print(f"Final Merge Sort array is: ",sorted_array)

# Complexity of Merge Sort
            
| Case             | Description              | Time Complexity |
| ---------------- | ------------------------ | --------------- |
| **Best Case**    | Array is already sorted  | **O(n log n)**  |
| **Average Case** | Random order of elements | **O(n log n)**  |
| **Worst Case**   | Array is reverse sorted  | **O(n log n)**  |
