
def linear_search(arr, target):

    for i in range(len(arr)):

        # Compare current element with target
        if arr[i] == target:
            return i

    # Target was not found
    return -1


# Example usage
numbers = [10, 25, 30, 45, 50]

target = 30

result = linear_search(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")