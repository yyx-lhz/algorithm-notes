# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)   # 哑节点，处理删除头节点的情况
        slow = dummy
        fast = head

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # 两指针保持距离，一起走到 fast 尽头
        while fast:
            slow = slow.next
            fast = fast.next

        # slow 此时在目标节点的前一个 → 跳过目标节点
        slow.next = slow.next.next

        return dummy.next
