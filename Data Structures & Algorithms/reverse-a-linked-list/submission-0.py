# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            temp = node
            next_node = node.next
            if prev == None:
                node.next = None
            else:
                node.next = prev
            prev = temp
            node = next_node
        return prev
        