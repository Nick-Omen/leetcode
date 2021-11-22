from typing import List
from unittest import TestCase


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == n:
                return True
            if i > n:
                return False

            for word in wordDict:
                if i + len(word) > n:
                    continue
                if word == s[i:i + len(word)]:
                    dp[i] = dfs(i + len(word))
                    if dp[i]:
                        return True

            dp[i] = False
            return dp[i]

        return dfs(0)


class TestSolution(TestCase):
    def test_solution(self):
        self.assertTrue(Solution().wordBreak("leetcode", ["leet", "code"]))
        self.assertTrue(Solution().wordBreak("applepenapple", ["apple", "pen"]))
        self.assertTrue(Solution().wordBreak("dogs", ["dog", "s", "gs"]))
        self.assertFalse(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
