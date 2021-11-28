from typing import List
from unittest import TestCase


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        out = [[1], [1, 1]]
        for i in range(2, numRows):
            sub = [1]
            for j in range(1, i):
                sub.append(out[i - 1][j - 1] + out[i - 1][j])
            sub.append(1)
            out.append(sub)
        return out


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], Solution().generate(5))
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]], Solution().generate(4))
        self.assertEqual([[1]], Solution().generate(1))
