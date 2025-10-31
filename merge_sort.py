def merge_sort(arr):
    # if the array length is 0 or 1, the the array is already sorted
    if len(arr) <= 1:
        return arr
        
    mid = len(arr)//2
    
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_sorted_arr = merge_sort(left_half)
    right_sorted_arr = merge_sort(right_half)
    
    return merge(left_sorted_arr, right_sorted_arr)
    
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
            
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
    
    
if __name__ == "__main__":
    arr = [10, 3,100, 55,32,27, 12,36]
    
    sorted_array = merge_sort(arr)
    print(f"Final Merge Sort array is: ",sorted_array)
            
