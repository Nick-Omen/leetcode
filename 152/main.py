from typing import List
from unittest import TestCase


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_sub = max(nums)
        cur_min, cur_max = 1, 1
        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
            _cur_max = n * cur_max
            cur_max = max(_cur_max, n * cur_min, n)
            cur_min = min(n * cur_min, _cur_max, n)
            max_sub = max(max_sub, cur_max)
        return max_sub


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(6, Solution().maxProduct([2, 3, -2, 4]))
        self.assertEqual(0, Solution().maxProduct([-2, 0, -1]))
        self.assertEqual(3, Solution().maxProduct([-3, -1, -1]))
        self.assertEqual(2, Solution().maxProduct([0, 2]))
        self.assertEqual(24, Solution().maxProduct([-2, 3, -4]))
