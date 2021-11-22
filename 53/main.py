from typing import List
from unittest import TestCase


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sub = 0
        for n in nums:
            if cur_sub < 0:
                cur_sub = 0
            cur_sub += n
            max_sub = max(max_sub, cur_sub)
        return max_sub


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(6, Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(1, Solution().maxSubArray([1]))
        self.assertEqual(23, Solution().maxSubArray([5, 4, -1, 7, 8]))
        self.assertEqual(21, Solution().maxSubArray([2, 3, 4, 5, 7]))
