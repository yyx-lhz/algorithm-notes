from typing import Optional

# Definition for singly-linked list (由 LeetCode 提供).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if not head or not head.next:
            return head

        # slow 停在左半段的最后一个节点。
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next
        slow.next = None  # 先保存右半段入口，再断开链表。

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        cur = dummy

        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        # 至少一边已经为空，直接接上另一边的剩余链表。
        cur.next = left if left else right
        return dummy.next
