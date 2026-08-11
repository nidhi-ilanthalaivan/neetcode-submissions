# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            # define next node 
            next_node = curr.next
            # reverse pointer next is now equal to prev
            curr.next = prev
            # prev is now defined as curr as its getting incremented to next one
            prev = curr
            # and curr is now the next one getting incremented obvi
            curr = next_node
        
        return prev
       