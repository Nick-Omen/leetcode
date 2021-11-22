from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                out += prices[i + 1] - prices[i]
        return max(0, out)


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(7, Solution().maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, Solution().maxProfit([1, 2, 3, 4, 5]))
        self.assertEqual(0, Solution().maxProfit([7, 6, 4, 3, 1]))
