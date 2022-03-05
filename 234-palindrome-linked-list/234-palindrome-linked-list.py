# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        count=0
        itr=head
        while itr:
            stack.append(itr.val)
            count+=1
            itr=itr.next
        print(stack)
        return stack==stack[::-1]