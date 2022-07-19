# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_count(head):
            count=0
            while head:
                head=head.next
                count+=1
            return count
        countA=get_count(headA)
        countB=get_count(headB)
        while countA!=countB:
            if countA>countB:
                headA=headA.next
                countA-=1
            elif countB>countA:
                headB=headB.next
                countB-=1
        while headA and headB:
            if headA==headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next
        return None                