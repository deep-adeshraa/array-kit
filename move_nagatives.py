# Move all negative numbers to beginning and positive to end with constant extra space
# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
# Examples :

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

# Note: Order of elements are not important

def move_nagatives(arr):
    index = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1

    return arr


arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(move_nagatives(arr))
