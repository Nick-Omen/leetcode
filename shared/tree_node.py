from typing import Optional, List
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def as_list(self) -> List[int]:
        queue = [self]
        items = []

        while len(queue) > 0:
            copy = queue[:]
            queue = []

            for item in copy:
                if item is None:
                    items.append(None)
                    queue.append(None)
                    queue.append(None)
                else:
                    items.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)

            if all((x is None for x in queue)):
                break
        while items[-1] is None:
            items.pop()
        return items

    @classmethod
    def from_list(cls, values: List[Optional[int]]) -> Optional['TreeNode']:
        """Create BT from list of values."""
        n = len(values)
        if n == 0:
            return None

        def inner(index: int = 0) -> Optional['TreeNode']:
            """Closure function using recursion bo build tree"""
            if n <= index or values[index] is None:
                return None

            node = TreeNode(values[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

        return inner()

    def __str__(self):
        return f'TreeNode<{self.val=},{self.left=},{self.right=}>'


class TreeNodeTestCase(TestCase):
    def setUp(self) -> None:
        values = [1]
        root = TreeNode.from_list(values)
        self.assertEqual(1, root.val)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)
        self.assertEqual(values, root.as_list())

        values = [1, 2]
        root = TreeNode.from_list(values)
        self.assertEqual(1, root.val)
        self.assertIsNotNone(root.left)
        self.assertEqual(2, root.left.val)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertIsNone(root.right)
        self.assertEqual(values, root.as_list())

        values = [1, None, 2]
        root = TreeNode.from_list(values)
        self.assertEqual(1, root.val)
        self.assertIsNone(root.left)
        self.assertIsNotNone(root.right)
        self.assertEqual(2, root.right.val)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.right.right)
        self.assertEqual(values, root.as_list())

        values = [1, 2, 3]
        root = TreeNode.from_list(values)
        self.assertEqual(1, root.val)
        self.assertIsNotNone(root.left)
        self.assertEqual(2, root.left.val)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertIsNotNone(root.right)
        self.assertEqual(3, root.right.val)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.right.right)
        self.assertEqual(values, root.as_list())

        values = [5, 3, 6, 2, 4, None, 7]
        root = TreeNode.from_list(values)
        self.assertEqual(values, root.as_list())
