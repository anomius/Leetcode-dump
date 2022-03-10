# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        itr1= l1
        itr2= l2
        cr=0
        k=t=ListNode(None)
        while itr1 and itr2:
            t.next=ListNode((itr1.val+itr2.val+cr)%10)
            cr=(itr1.val+itr2.val+cr)//10
            itr1=itr1.next
            itr2=itr2.next
            t=t.next
        if itr1:
            while itr1:
                t.next=ListNode((itr1.val+cr)%10)
                cr=(itr1.val+cr)//10
                itr1=itr1.next
                t=t.next
        if itr2:
            while itr2:
                t.next=ListNode((itr2.val+cr)%10)
                cr=(itr2.val+cr)//10
                itr2=itr2.next
                t=t.next
        if cr!=0:
            t.next=ListNode(cr)
        return k.next