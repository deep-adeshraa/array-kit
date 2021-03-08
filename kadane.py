# Kadane's Algorithm
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

# N = 5
# arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which
# is a contiguous subarray.
# Example 2:

# N = 4
# arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1
# of element (-1)

def max_subarray_sum(array):
    curr_max = 0
    max_so_far = float('-inf')

    for i in range(len(array)):

        curr_max = curr_max + array[i]

        if curr_max > max_so_far:
            max_so_far = curr_max

        if curr_max < 0:
            curr_max = 0

        print(max_so_far, curr_max)

    return max_so_far


array = [-21, -4, -3, -23, -1, -2, -4]
print(max_subarray_sum(array))
