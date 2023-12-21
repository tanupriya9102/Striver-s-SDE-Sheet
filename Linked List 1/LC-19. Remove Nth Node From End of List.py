class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      dummy = ListNode(0)  # Dummy node to handle the head case
      dummy.next = head
      s=dummy
      f=dummy
      c=0
      while(c<=n):
        c+=1
        f=f.next
      while(f is not None):
        s=s.next
        f=f.next
      s.next=s.next.next
      return dummy.next






      
