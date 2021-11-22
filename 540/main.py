from typing import List
from unittest import TestCase


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return nums[0]
        if n == 3:
            return nums[0] if nums[1] == nums[2] else nums[2]
        middle = n // 2
        if nums[middle] == nums[middle + 1]:
            if len(nums[:middle]) % 2 == 1:
                return self.singleNonDuplicate(nums[:middle])
            return self.singleNonDuplicate(nums[middle:])
        elif nums[middle] == nums[middle - 1]:
            if len(nums[:middle - 1]) % 2 == 1:
                return self.singleNonDuplicate(nums[:middle - 1])
            return self.singleNonDuplicate(nums[middle + 1:])
        return nums[middle]


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(2, Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
        self.assertEqual(9, Solution().singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 8, 8, 9]))
        self.assertEqual(10, Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
