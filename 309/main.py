from typing import List
from unittest import TestCase


class Solution:
    def __init__(self):
        self.cache = {}
        self.prices = []
        self.prices_len = 0

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.prices_len = len(self.prices)
        return self._maxProfit(0, True)

    def _maxProfit(self, i: int, is_buying: bool):
        if i >= self.prices_len:
            return 0
        k = f'{i}{"T" if is_buying else "F"}'
        if k in self.cache:
            return self.cache[k]

        waiting = self._maxProfit(i + 1, is_buying)
        if is_buying:
            profit = self._maxProfit(i + 1, not is_buying) - self.prices[i]
        else:
            profit = self._maxProfit(i + 2, not is_buying) + self.prices[i]
        self.cache[k] = max(waiting, profit)
        return self.cache[k]


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(3, Solution().maxProfit([1, 2, 3, 0, 2]))
        self.assertEqual(0, Solution().maxProfit([1]))
        self.assertEqual(15, Solution().maxProfit([4, 2, 4, 12, 2, 7, 12]))
