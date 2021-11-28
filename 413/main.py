from typing import List
from unittest import TestCase


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        cache = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cache[i] = 1 + cache[i - 1]
        return sum(cache)


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(3, Solution().numberOfArithmeticSlices([1, 2, 3, 4]))
        self.assertEqual(0, Solution().numberOfArithmeticSlices([1]))
        self.assertEqual(6, Solution().numberOfArithmeticSlices([1, 2, 3, 4, 5]))
