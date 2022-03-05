# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def rev(head):
            d=None
            itr=head
            while itr:
                nex=itr.next
                itr.next=d
                d=itr
                itr=nex
            return d
        
        # using fast and slow method
        fast,slow=head,head
        
        while (fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        
        
        slow=rev(slow.next)
        
        itr=head
        while itr and slow:
            if itr.val!=slow.val:
                return False
            slow=slow.next
            itr=itr.next
        return slow==None
    
            
        
                
            