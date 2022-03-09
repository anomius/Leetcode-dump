# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        fake = ListNode(0, head)
        pred = fake
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return fake.next