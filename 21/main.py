from typing import Optional

from shared import ListNode, ListNodeTestCase


class Solution:
    # def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     cur_l1 = l1
    #     cur_l2 = l2
    #     vals = []
    #     while cur_l1 is not None or cur_l2 is not None:
    #         if cur_l1 is not None:
    #             vals.append(cur_l1.val)
    #             cur_l1 = cur_l1.next
    #         if cur_l2 is not None:
    #             vals.append(cur_l2.val)
    #             cur_l2 = cur_l2.next
    #     node = None
    #     for n in sorted(vals, reverse=True):
    #         node = ListNode(val=n, next=node)
    #     return node

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        if (l1 is None and l2 is not None) or (l2 is None and l1 is not None):
            return l1 or l2
        cur_l1 = l1
        cur_l2 = l2

        sorted_list = []

        while cur_l1 is not None or cur_l2 is not None:
            if cur_l1 is not None and cur_l2 is not None:
                if cur_l1.val < cur_l2.val:
                    sorted_list.append(cur_l1.val)
                    cur_l1 = cur_l1.next
                else:
                    sorted_list.append(cur_l2.val)
                    cur_l2 = cur_l2.next
            elif cur_l1 is not None and cur_l2 is None:
                sorted_list.append(cur_l1.val)
                cur_l1 = cur_l1.next
            else:
                sorted_list.append(cur_l2.val)
                cur_l2 = cur_l2.next
        head = None
        for n in sorted_list[::-1]:
            head = ListNode(val=n, next=head)
        return head


class TestSolution(ListNodeTestCase):
    def test_solution(self):
        res = Solution().mergeTwoLists(
            ListNode.create_from_list([1, 2, 4]),
            ListNode.create_from_list([1, 3, 4])
        )
        self.assertEqual([1, 1, 2, 3, 4, 4], res.to_list())

        res = Solution().mergeTwoLists(
            ListNode.create_from_list([]),
            ListNode.create_from_list([])
        )
        self.assertIsNone(res)

        res = Solution().mergeTwoLists(
            ListNode.create_from_list([]),
            ListNode.create_from_list([0])
        )
        self.assertEqual([0], res.to_list())
