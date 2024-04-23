# Question 12:
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# defining the function
def rearrange(nums, k):
    """
    Rotating the array to the right by k steps in-place.

    Args:
        nums(list): input array.
        k(int): number of steps to rotate.

    Returns:
    nums(list): Rotated list
    """
    n = len(nums)
     # Ensuring k is within the range of the array length
    k = k % n 
    
    # Reversing the entire array
    nums.reverse()
    
    # Reversing the first k elements
    nums[:k] = reversed(nums[:k])
    
    # Reversing the remaining elements
    nums[k:] = reversed(nums[k:])

    return nums

# Testing the function
num = [1, 2, 3, 4, 5, 6, 7]
n = 3
result = rearrange(num, n)
print(result) 