from typing import Optional, List
from unittest import TestCase


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'ListNode<{self.val=}>'

    @classmethod
    def create_from_list(cls, values: List[int]) -> 'ListNode':
        node: Optional[ListNode] = None
        for n in values[::-1]:
            node = ListNode(val=n, next=node)
        return node

    def to_list(self) -> List[int]:
        out: List[int] = []
        node = self
        while node is not None:
            out.append(node.val)
            node = node.next
        return out


class ListNodeTestCase(TestCase):
    def setUp(self) -> None:
        values = []
        root = ListNode.create_from_list(values)
        self.assertIsNone(root)

        values = [1]
        root = ListNode.create_from_list(values)
        self.assertIsNotNone(root)
        self.assertEqual(1, root.val)
        self.assertIsNone(root.next)
        self.assertEqual(values, root.to_list())

        values = [1, 2]
        root = ListNode.create_from_list(values)
        self.assertIsNotNone(root)
        self.assertEqual(1, root.val)
        self.assertIsNotNone(root.next)
        self.assertEqual(2, root.next.val)
        self.assertIsNone(root.next.next)
        self.assertEqual(values, root.to_list())
