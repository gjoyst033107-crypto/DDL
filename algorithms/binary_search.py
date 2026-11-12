
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        # Find middle index
        mid = (low + high) // 2

        # Check if target is found
        if arr[mid] == target:
            return mid

        # Search the right half
        elif arr[mid] < target:
            low = mid + 1

        # Search the left half
        else:
            high = mid - 1

    # Target was not found
    return -1


# Example usage
numbers = [10, 20, 30, 40, 50, 60, 70]

target = 50

result = binary_search(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
