from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = [0] * n
        sell = [0] * n

        buy[0] = prices[0]

        for i in range(1, n):
            buy[i] = min(buy[i - 1], prices[i] - sell[i - 1])
            sell[i] = max(sell[i - 1], prices[i] - buy[i - 1] - fee)

        return sell[-1]


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(8, Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
        self.assertEqual(6, Solution().maxProfit([1, 3, 7, 5, 10, 3], 3))
