from typing import List
from unittest import TestCase


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(28, Solution().uniquePaths(3, 7))
        self.assertEqual(3, Solution().uniquePaths(2, 3))
