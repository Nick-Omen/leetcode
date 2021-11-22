from typing import List, Optional
from unittest import TestCase

from shared import TreeNode


class Solution:
    def buildTree(self, root: Optional[TreeNode]) -> List[int]:
        return []


class TestSolution(TestCase):
    def test_solution(self):
        root = TreeNode.from_list([1, None, 2, 3])
        self.assertEqual([1, 3, 2], Solution().buildTree(root))
        root = TreeNode.from_list([])
        self.assertIsNone(root)
        self.assertEqual([], Solution().buildTree(root))
        root = TreeNode.from_list([1])
        self.assertEqual([1], Solution().buildTree(root))
