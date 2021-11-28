import math
from collections import Counter
from typing import List
from unittest import TestCase


class UnionFind:
    def __init__(self, n):
        self.data = list(range(n))

    def find(self, x):
        while self.data[x] != x:
            self.data[x] = self.data[self.data[x]]
            x = self.data[x]
        return x

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        self.data[root1] = self.data[root2]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        p = max(nums) + 1
        u = UnionFind(p)

        for num in nums:
            for i in range(2, int(math.sqrt(num) + 1)):
                if num % i == 0:
                    u.union(num, i)
                    u.union(num, num // i)

        counter = Counter([u.find(num) for num in nums])
        return max(counter.values())


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(4, Solution().largestComponentSize([4, 6, 15, 35]))
        self.assertEqual(2, Solution().largestComponentSize([20, 50, 9, 63]))
        self.assertEqual(8, Solution().largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]))
