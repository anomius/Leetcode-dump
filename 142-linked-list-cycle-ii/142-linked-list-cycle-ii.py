# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow ,fast = head,head
        while slow and fast:
            slow=slow.next
            if fast.next:
                fast=fast.next.next 
            else: 
                return None
            if slow==fast:
                cur=head
                count=0
                while cur!=slow:
                    cur=cur.next
                    slow=slow.next
                    count+=1
                return cur
        
        return None
            
            