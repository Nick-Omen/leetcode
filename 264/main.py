from typing import List
from unittest import TestCase


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        cache = [0] * n
        cache[0] = 1

        u2 = u3 = u5 = 0

        multiple_2 = 2
        multiple_3 = 3
        multiple_5 = 5

        for i in range(1, n):
            cache[i] = min(multiple_2, multiple_3, multiple_5)

            if cache[i] == multiple_2:
                u2 += 1
                multiple_2 = cache[u2] * 2

            if cache[i] == multiple_3:
                u3 += 1
                multiple_3 = cache[u3] * 3

            if cache[i] == multiple_5:
                u5 += 1
                multiple_5 = cache[u5] * 5

        return cache[n - 1]


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(12, Solution().nthUglyNumber(10))
        self.assertEqual(1, Solution().nthUglyNumber(1))
        self.assertEqual(9, Solution().nthUglyNumber(8))
        self.assertEqual(1536, Solution().nthUglyNumber(100))
