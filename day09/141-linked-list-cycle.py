# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next         # 慢指针走 1 步
            fast = fast.next.next    # 快指针走 2 步

            if slow == fast:         # 追上了 → 有环
                return True

        return False                 # fast 到尽头 → 无环
