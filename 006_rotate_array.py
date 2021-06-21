"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


def rotate_array(nums, k):

    k = k % len(nums)
    nums = nums[::-1]  # reverse array
    nums[0:k] = nums[0:k][::-1]
    nums[k:] = nums[k:][::-1]
    return nums


print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
