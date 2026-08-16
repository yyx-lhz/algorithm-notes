# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # 第一阶段：快慢指针判断有环并相遇
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # 有环。第二阶段：slow 放回 head，两指针同速走
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow   # 再次相遇处 = 环入口

        return None   # fast 到尽头，无环
