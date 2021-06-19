"""
Given an array arr[0 . . . n-1]. We need to efficiently find the minimum and maximum
value from index 0 to query index.
"""


def max_from_range(N, Q):
    maximum = N[0]
    for i in range(len(N)):
        maximum = max(maximum, N[i])
        N[i] = maximum
    for i in range(len(Q)):
        print(f"Max from 0 to {Q[i]}:", N[Q[i]])


max_from_range([2, 1, 4, 6, 2, 4, 7, 8, 22, 2, 4], (5,7,2))
