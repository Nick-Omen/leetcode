from typing import List
from unittest import TestCase


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        pass


class TestSolution(TestCase):
    def test_solution(self):
        self.assertTrue([1, 2], Solution().largestDivisibleSubset([1, 2, 3]))
        self.assertEqual([1, 2, 4, 8], Solution().largestDivisibleSubset([1, 2, 4, 8]))
        self.assertEqual([4, 8, 16], Solution().largestDivisibleSubset([3, 4, 16, 8]))
