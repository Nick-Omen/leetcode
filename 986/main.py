from typing import List
from unittest import TestCase


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fln = len(firstList)
        sln = len(secondList)
        if fln == 0 or sln == 0:
            return []
        i = 0
        j = 0
        out = []
        while i < fln and j < sln:
            fl = firstList[i]
            sl = secondList[j]
            intersection = [max(fl[0], sl[0]), min(fl[1], sl[1])]
            if intersection[0] <= intersection[1]:
                out.append(intersection)
            if fl[1] < sl[1]:
                i += 1
            elif fl[1] == sl[1]:
                i += 1
                j += 1
            else:
                j += 1
        return out


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
            Solution().intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                                            [[1, 5], [8, 12], [15, 24], [25, 26]])
        )
        self.assertEqual([], Solution().intervalIntersection([[1, 3], [5, 9]], []))
        self.assertEqual([], Solution().intervalIntersection([], [[4, 8], [10, 12]]))
        self.assertEqual([[3, 7]], Solution().intervalIntersection([[1, 7]], [[3, 10]]))
