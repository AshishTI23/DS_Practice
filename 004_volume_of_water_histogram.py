"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""


def max_volume_of_water(Array):
    right_max = []
    left_max = []
    r_max = Array[0]
    l_max = Array[len(Array) - 1]
    for i in range(len(Array)):
        r_max = max(Array[i], r_max)
        right_max.append(r_max)
    for i in range(len(Array) - 1, -1, -1):
        print(i)
        l_max = max(Array[i], l_max)
        left_max.append(l_max)
    left_max = left_max[::-1]
    max_volume = 0
    for (l, r, Array) in zip(left_max, right_max, Array):
        max_volume += min(l, r) - Array
    return max_volume


print(max_volume_of_water([2, 3, 4, 6, 10, 1, 2, 10, 5]))
