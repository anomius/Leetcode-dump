class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        l=[]
        while x>0:
            rem=x%10
            x=x//10
            l.append(rem)
        for i in range(len(l)//2):
            if l[i]!=l[-1-i]:
                return False
        return True
        