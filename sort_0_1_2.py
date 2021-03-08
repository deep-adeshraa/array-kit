# LB- Array - 4 : https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

# Sort an array of 0s, 1s and 2s

# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2

# Input:
# N = 3
# arr[] = {0 1 0}
# Output:
# 0 0 1


def sort012(self, arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    
    for i in arr:
        if i == 0:
            cnt0 += 1
        elif i == 1:
            cnt1 += 1
        else:
            cnt2+=1
    
    for i in range(len(arr)):
        if cnt0 != 0:
            arr[i] = 0
            cnt0 -=1
        elif cnt1 != 0:
            arr[i] = 1
            cnt1 -=1
        else:
            arr[i] = 2
    
    return arr



print(sort012(0, 2, 1, 2, 0))
