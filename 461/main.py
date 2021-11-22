from unittest import TestCase


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x > y:
            X = f'{x:b}'
            Y = f'{y:0{len(X)}b}'
        else:
            Y = f'{y:b}'
            X = f'{x:0{len(Y)}b}'
        out = 0
        for i in range(len(X)):
            if X[i] != Y[i]:
                out += 1
        return out


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(2, Solution().hammingDistance(1, 4))
        self.assertEqual(1, Solution().hammingDistance(3, 1))
        self.assertEqual(2, Solution().hammingDistance(4, 14))
