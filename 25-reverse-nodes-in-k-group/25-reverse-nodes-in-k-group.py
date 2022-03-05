# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        itr=head
        count=0
        temp=ListNode(0)
        temp.next=head
        pre=temp
        while itr:
            itr=itr.next
            count+=1
            
        while count>=k:
            print(count)
            itr=pre.next
            end=itr.next
            for i in range(k-1):
                itr.next=end.next
                end.next=pre.next
                pre.next=end
                end=itr.next
            pre=itr
            count-=k
        return temp.next
            
            
        
        
                
                
                