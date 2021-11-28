from typing import List
from unittest import TestCase


class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {'': 1}

        def ways(subs):
            if subs in memo:
                return memo[subs]
            if subs[0] == '0':
                return 0

            if len(subs) == 1 or int(subs[0]) >= 3:
                output = ways(subs[1:])
            elif int(subs[0:2]) > 26:
                output = ways(subs[1:])
            else:
                output = ways(subs[1:]) + ways(subs[2:])

            memo[subs] = output
            return output

        return ways(s)


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(2, Solution().numDecodings("12"))
        self.assertEqual(3, Solution().numDecodings("226"))
        self.assertEqual(0, Solution().numDecodings("0"))
        self.assertEqual(0, Solution().numDecodings("06"))
        self.assertEqual(3, Solution().numDecodings("1201234"))
