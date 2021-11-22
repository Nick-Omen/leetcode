from typing import List
from unittest import TestCase


class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height) - 1

        prev = height[0]

        prev_index = 0
        water = 0

        temp = 0
        for i in range(1, size + 1):
            if height[i] >= prev:
                prev = height[i]
                prev_index = i

                temp = 0
            else:
                water += prev - height[i]
                temp += prev - height[i]

        if prev_index < size:
            water -= temp
            prev = height[size]
            for i in range(size, prev_index - 1, -1):
                if height[i] >= prev:
                    prev = height[i]
                else:
                    water += prev - height[i]

        return water


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(6, Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(9, Solution().trap([4, 2, 0, 3, 2, 5]))
