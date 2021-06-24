"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).
"""


def maxProfit(prices) -> int:
    prefix_profit = []
    suffix_profit = []
    min_buy = prices[0]
    max_sell = prices[-1]
    max_prefix_profit = 0
    max_suffix_profit = 0
    for i in range(len(prices)):
        min_buy = min(min_buy, prices[i])
        max_prefix_profit = max(max_prefix_profit, prices[i] - min_buy)
        prefix_profit.append(max_prefix_profit)
    for i in range(len(prices) - 1, -1, -1):
        max_sell = max(max_sell, prices[i])
        max_suffix_profit = max(max_suffix_profit, max_sell - prices[i])
        suffix_profit.append(max_suffix_profit)
    suffix_profit = suffix_profit[::-1]
    total_profit = 0
    for prefix, suffix in zip(prefix_profit, suffix_profit):
        total_profit = max(total_profit, prefix + suffix)

    return total_profit


print(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
