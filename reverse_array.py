# LB- Array - 1 : https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

# Given an array (or string), the task is to reverse the array/string.
# Examples :


# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

def reverse(array):
    # we can simply use in-built python function but that is not valid approach

    # try to do in-place reversal
    length = len(array)
    i = 0
    j = length - 1

    while i <= j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    return array


ans = reverse([2, 3, 4, 5, 6])
print(ans)
