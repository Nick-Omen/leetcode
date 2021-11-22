from typing import List
from unittest import TestCase


class Solution:
    # def maxSubarraySumCircular(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n < 2:
    #         return nums[0]
    #     max_sub = -10001
    #     for i in range(n):
    #         max_sub = max(max_sub, self._maxSubarraySumCircular([*nums[i:], *nums[:i]]))
    #     return max_sub
    #
    # def _maxSubarraySumCircular(self, nums: List[int]) -> int:
    #     max_sub = nums[0]
    #     cur_sub = 0
    #     for n in nums:
    #         if cur_sub < 0:
    #             cur_sub = 0
    #         cur_sub += n
    #         max_sub = max(max_sub, cur_sub)
    #     return max_sub

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_continuous_sum = nums[0]
        current_max = -10001

        min_continuous_sum = nums[0]
        current_min = 10001

        total = 0

        for num in nums:
            total += num

            current_max = max(current_max + num, num)
            max_continuous_sum = max(max_continuous_sum, current_max)

            current_min = min(current_min + num, num)
            min_continuous_sum = min(min_continuous_sum, current_min)

        if total == min_continuous_sum:
            return max_continuous_sum
        return max(total - min_continuous_sum, max_continuous_sum)


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(3, Solution().maxSubarraySumCircular([1, -2, 3, -2]))
        self.assertEqual(10, Solution().maxSubarraySumCircular([5, -3, 5]))
        self.assertEqual(4, Solution().maxSubarraySumCircular([3, -1, 2, -1]))
        self.assertEqual(3, Solution().maxSubarraySumCircular([3, -2, 2, -3]))
        self.assertEqual(-1, Solution().maxSubarraySumCircular([-2, -3, -1]))
        self.assertEqual(15, Solution().maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4]))
