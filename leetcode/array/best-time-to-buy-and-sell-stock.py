import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # price 를 계속 비교하여 최솟값 설정, profit 최대값 비교
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            print(min_price, profit)

        return profit


s = Solution()
print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
# print(s.maxProfit(prices=[7, 6, 4, 3, 1]))
# print(s.maxProfit(prices=[2, 4, 1]))
