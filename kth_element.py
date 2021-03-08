# K’th Smallest/Largest Element in Unsorted Array
 
# Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

# Examples:  

# Input: arr[] = {7, 10, 4, 3, 20, 15} 
# k = 3 
# Output: 7

# Input: arr[] = {7, 10, 4, 3, 20, 15} 
# k = 4 
# Output: 10 
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

import heapq

def kth_smallest(arr, k):
    heapq.heapify(arr) 
    k -=1
    
    while k:
        item = heapq.heappop(arr)
        
        k -=1
    
    return heapq.heappop(arr)

def kth_largest(arr, k):
    heapq._heapify_max(arr)

    k -=1
    while k:
        item = heapq._heappop_max(arr)
        
        k -=1
    
    return heapq._heappop_max(arr)


print(kth_smallest([1,2,3,4], 4))

print(kth_largest([1,2,3,4], 4))