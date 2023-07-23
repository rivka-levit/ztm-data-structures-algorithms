"""
You are given an array prices where prices[i] is the price of a given
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Full description:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    min_price = float('inf')
    max_prof = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_prof:
            max_prof = profit

    return max_prof

