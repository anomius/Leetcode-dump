class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = [0] *(max(nums)+1)
        for i in nums:
            d[i] += i
        prev,prever = 0,0 
        for i in d:
            cur = max(prev,prever+i)
            prever = prev
            prev = cur 
        return max(cur,prever)
        