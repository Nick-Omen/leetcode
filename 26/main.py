from typing import Optional, List
from unittest import TestCase


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_l = len(nums)
        offset = 0
        for i in range(1, nums_l):
            j = i - offset
            if nums[j] != nums[j - 1]:
                continue
            offset += 1
            nums.pop(j - 1)
            nums.append('_')
        return nums_l - offset


class TestSolution(TestCase):

    def test_solution(self):
        nums = [1, 1, 2]
        self.assertEqual(2, Solution().removeDuplicates(nums))
        self.assertEqual([1, 2, '_'], nums)
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(5, Solution().removeDuplicates(nums))
        self.assertEqual([0, 1, 2, 3, 4, '_', '_', '_', '_', '_'], nums)
