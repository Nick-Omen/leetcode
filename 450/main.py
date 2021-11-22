from typing import List, Optional
from unittest import TestCase

from shared import TreeNode, TreeNodeTestCase


class Solution:
    @staticmethod
    def minValueNode(node: TreeNode):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if root.val == key:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.minValueNode(root.right)

            root.val = temp.val

            root.right = self.deleteNode(root.right, temp.val)
        else:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
        return root


class TestSolution(TreeNodeTestCase):
    def test_solution(self):
        root = TreeNode.from_list([5, 3, 6, 2, 4, None, 7])
        res = Solution().deleteNode(root, 3)
        self.assertEqual([5, 4, 6, 2, None, None, 7], res.as_list())

        root = TreeNode.from_list([5, 3, 6, 2, 4, None, 7])
        res = Solution().deleteNode(root, 0)
        self.assertEqual([5, 3, 6, 2, 4, None, 7], res.as_list())

        root = TreeNode.from_list([])
        res = Solution().deleteNode(root, 0)
        self.assertIsNone(res)
