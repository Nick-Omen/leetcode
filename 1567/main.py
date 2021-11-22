from typing import List
from unittest import TestCase


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        size = len(nums)
        pos, neg = [0 for _ in range(size)], [0 for _ in range(size)]

        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1

        for idx, number in enumerate(nums[1:], 1):
            if number > 0:
                pos[idx] = pos[idx-1] + 1
                if neg[idx-1]:
                    neg[idx] = neg[idx-1] + 1
            elif number < 0:
                neg[idx] = pos[idx-1] + 1
                if neg[idx-1]:
                    pos[idx] = neg[idx-1] + 1
        return max(pos)


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(4, Solution().getMaxLen([1, -2, -3, 4]))
        self.assertEqual(3, Solution().getMaxLen([0, 1, -2, -3, -4]))
        self.assertEqual(2, Solution().getMaxLen([-1, -2, -3, 0, 1]))
        self.assertEqual(4, Solution().getMaxLen([1, 2, 3, 5, -6, 4, 0, 10]))
