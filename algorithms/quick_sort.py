
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    # Select the last element as pivot
    pivot = arr[-1]

    # Separate smaller and larger elements
    left = []
    right = []

    for number in arr[:-1]:

        if number <= pivot:
            left.append(number)
        else:
            right.append(number)

    # Recursively sort both sides
    return quick_sort(left) + [pivot] + quick_sort(right)



# Example usage
numbers = [10, 7, 8, 9, 1, 5]

print("Original Array:", numbers)
print("Sorted Array:", quick_sort(numbers))
