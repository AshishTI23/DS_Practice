"""
Suppose, you are given an array containing N elements and there is Q
number of queries. Each query contains L and R , (L, R)
Find the sum of all the elements in the range L to R (both inclusive)
"""


def range_sum(N, Q):

    for i in range(1, len(N)):
        N[i] += N[i - 1]
    # N = [1, 3, 5, 9, 15, 20, 23]
    for q in Q:
        L = q[0] - 1
        R = q[1] - 1
        print(f"Sum [{L+1}, {R+1}]: ", N[R] - (N[L - 1] if L - 1 >= 0 else 0))


range_sum([1, 2, 2, 4, 6, 5, 3], [[1, 3], [2, 4], [4, 7]])
