# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1=ListNode(None)
        head=h1
        itr1,itr2=l1,l2
        val,car=0,0
        while itr1 and itr2:
            val=(itr1.val+itr2.val+car)%10
            car=(itr1.val+itr2.val+car)//10
            itr1,itr2=itr1.next,itr2.next
            h1.next=ListNode(val)
            h1=h1.next
        while itr1:
            val=(itr1.val+car)%10
            car=(itr1.val+car)//10
            itr1=itr1.next
            h1.next=ListNode(val)
            h1=h1.next
        while itr2:
            val=(itr2.val+car)%10
            car=(itr2.val+car)//10
            itr2=itr2.next
            h1.next=ListNode(val)
            h1=h1.next
        if car!=0:
            h1.next=ListNode(car)
        return head.next