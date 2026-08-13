# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        pre = None
        current = head

        while current:
            next_node = current.next    # 1. 先保存下一个节点
            current.next = pre          # 2. 当前节点反向指向
            pre = current               # 3. pre 前移
            current = next_node         # 4. current 前移

        return pre
