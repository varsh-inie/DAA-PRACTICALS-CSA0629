def min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    elif high == low + 1:
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])

    else:
        mid = (low + high) // 2

        min1, max1 = min_max(arr, low, mid)
        min2, max2 = min_max(arr, mid + 1, high)

    return min(min1, min2), max(max1, max2)

# Example usage:
arr = [5, 3, 8, 2, 10, 7]
min_val, max_val = min_max(arr, 0, len(arr) - 1)

print("Minimum value:", min_val)
print("Maximum value:", max_val)
