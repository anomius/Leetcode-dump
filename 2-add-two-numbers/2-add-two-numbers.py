class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        curr = res
        num = 0
        while l1 or l2 or num > 0:
            num += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            curr.next = ListNode(num % 10)
            num //= 10 # floor division
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next