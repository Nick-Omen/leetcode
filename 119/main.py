from typing import List
from unittest import TestCase


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        index = 2
        prev = [1, 1]
        while index <= rowIndex:
            cur = [1]
            for j in range(1, index):
                cur.append(prev[j - 1] + prev[j])
            cur.append(1)
            prev = cur
            index += 1
        return prev


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual([1, 4, 6, 4, 1], Solution().getRow(4))
        self.assertEqual([1, 3, 3, 1], Solution().getRow(3))
        self.assertEqual([1, 2, 1], Solution().getRow(2))
        self.assertEqual([1, 1], Solution().getRow(1))
        self.assertEqual([1], Solution().getRow(0))
