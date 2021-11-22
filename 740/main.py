from collections import Counter
from typing import List
from unittest import TestCase


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        print(list(nums_counter.elements()))
        return 0


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(6, Solution().deleteAndEarn([3, 4, 2]))
        self.assertEqual(9, Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))
