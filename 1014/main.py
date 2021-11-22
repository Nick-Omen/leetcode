from typing import List
from unittest import TestCase


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        score = local_score = 0
        for i in range(len(values)):
            score = max(score, local_score + values[i] - i)
            local_score = max(local_score, values[i] + i)
        return score


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(11, Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))
        self.assertEqual(2, Solution().maxScoreSightseeingPair([1, 2]))
