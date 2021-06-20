def maxChunksToSorted(arr) -> int:
    max_chunk = 0
    max_item_idx = 0
    for i in range(len(arr)):
        max_item_idx = max(max_item_idx, arr[i])
        if max_item_idx == i:
            max_chunk += 1
    return max_chunk