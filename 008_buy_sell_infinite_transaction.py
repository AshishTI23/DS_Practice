"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock (infinite transactions allowed).

Return the maximum profit you can achieve from this transaction . If you cannot achieve any 
profit, return 0.
"""


def buy_sell_stock(array):
    buy_idx = sell_idx = total_profit = i = transaction = 0
    while i < len(array):
        if i < len(array) - 1 and array[i] <= array[i + 1]:
            sell_idx += 1
            i += 1
        else:
            profit = array[sell_idx] - array[buy_idx]
            buy_idx = sell_idx = i = i + 1
            if profit > 0:
                total_profit += profit
                transaction += 1
    return (transaction, total_profit)


print(buy_sell_stock([1, 3, 2, 4, 6, 1, 8]))
