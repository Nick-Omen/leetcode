from typing import List
from unittest import TestCase


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            self._rob(nums[1:]),
            self._rob(nums[:-1])
        )

    def _rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        mv = [0 for _ in nums]

        mv[0] = nums[0]
        mv[1] = max(nums[0], nums[1])

        for i in range(2, n):
            mv[i] = max(nums[i] + mv[i - 2], mv[i - 1])
        return max(mv)


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(3, Solution().rob([2, 3, 2]))
        self.assertEqual(4, Solution().rob([1, 2, 3, 1]))
        self.assertEqual(3, Solution().rob([1, 2, 3]))
        self.assertEqual(3, Solution().rob([1, 2, 1, 1]))
