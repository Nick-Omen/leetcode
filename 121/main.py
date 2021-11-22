from typing import List
from unittest import TestCase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        curr = 0
        for i in range(len(prices) - 1):
            if curr < 0:
                curr = prices[i + 1] - prices[i]
            else:
                curr += prices[i + 1] - prices[i]
            out = max(curr, out)
        return max(0, out)


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(5, Solution().maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(0, Solution().maxProfit([7, 6, 4, 3, 1]))
