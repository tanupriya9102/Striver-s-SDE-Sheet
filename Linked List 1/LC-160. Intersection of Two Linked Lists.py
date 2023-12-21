# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1=headA
        d2=headB

        while d1!=d2:
            if d1 is None:
                d1=headB
            elif d1 is not None:
                d1=d1.next

            if d2 is None:
                d2=headA
            elif d2 is not None:
                d2=d2.next
            
        return d1

             
