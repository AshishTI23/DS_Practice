"""
Given an array A[] with N elements , you need to find the sum all sub arrays of array A.
"""


def subarraySum(a, n):
    # code here
    total_sum = 0
    for i in range(n):
        total_sum += a[i] * (n - i) * (i + 1)
    return total_sum


A = [1, 2, 3, 4]
print(A, len(A))
