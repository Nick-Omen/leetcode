from typing import List
from unittest import TestCase


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        seq_start = seq_end = 0
        while seq_end < len(nums) - 1:
            if seq_start > seq_end:
                return False
            longest = 0
            for i in range(seq_start, seq_end + 1):
                longest = max(longest, i + nums[i])
            seq_start = seq_end + 1
            seq_end = longest
        return True


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(True, Solution().canJump([2, 3, 1, 1, 4]))
        self.assertEqual(False, Solution().canJump([3, 2, 1, 0, 4]))
        self.assertEqual(True, Solution().canJump([1, 2]))
