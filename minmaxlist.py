def find_max_min(arr, low, high):
    if low == high:  # Base case: Only one element in the sublist
        return arr[low], arr[low]

    elif high - low == 1:  # Base case: Two elements in the sublist
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])

    else:
        mid = (low + high) // 2
        max1, min1 = find_max_min(arr, low, mid)  # Recursively find max and min in the left sublist
        max2, min2 = find_max_min(arr, mid + 1, high)  # Recursively find max and min in the right sublist

        return max(max1, max2), min(min1, min2)  # Combine results


# Example usage:
arr = [5, 3, 9, 1, 7, 2, 8, 4, 6]
max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
