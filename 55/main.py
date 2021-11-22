from typing import List
from unittest import TestCase


class Solution:
    def jump(self, nums: List[int]) -> int:
        j = 0
        seq_start = seq_end = 0
        while seq_end < len(nums) - 1:
            longest = 0
            for i in range(seq_start, seq_end + 1):
                longest = max(longest, i + nums[i])
            seq_start = seq_end + 1
            seq_end = longest
            j += 1
        return j


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(2, Solution().jump([2, 3, 1, 1, 4]))
        self.assertEqual(2, Solution().jump([2, 3, 0, 1, 4]))
        self.assertEqual(0, Solution().jump([0]))
        self.assertEqual(2, Solution().jump([1, 2, 3]))
        self.assertEqual(3, Solution().jump([1, 1, 1, 1]))
