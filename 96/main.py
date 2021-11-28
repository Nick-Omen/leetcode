from typing import List
from unittest import TestCase


class Solution:
    def numTrees(self, n: int) -> int:
        cache = [1] * (n + 1)

        for node in range(2, n + 1):
            total = 0
            for root in range(1, node + 1):
                left = root - 1
                right = node - root
                total += cache[left] * cache[right]
            cache[node] = total
        return cache[n]


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(5, Solution().numTrees(3))
        self.assertEqual(1, Solution().numTrees(1))
