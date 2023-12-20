# Q.Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        f=head
        while(f is not None and f.next is not None):           
            s=s.next
            f=f.next.next

        return s
            
        
