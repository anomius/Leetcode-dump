# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while slow and fast:
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                break
            if slow==fast:
                cur=head
                while slow!=cur:
                    slow=slow.next
                    cur=cur.next
                return cur
        return None