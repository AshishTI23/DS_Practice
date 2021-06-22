"""
You are given an integer array arr of length n that represents a permutation of the integers 
in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. 
After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
"""

def maxChunksToSorted(arr) -> int:
    max_chunk = 0
    max_item_idx = 0
    for i in range(len(arr)):
        max_item_idx = max(max_item_idx, arr[i])
        if max_item_idx == i:
            max_chunk += 1
    return max_chunk