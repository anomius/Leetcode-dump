# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=None
        itr=head
        while itr:
            nex=itr.next
            itr.next=d
            d=itr
            itr=nex
        return d