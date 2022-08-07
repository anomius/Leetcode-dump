class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #order of O(N)
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in d.values():
            if j>1:
                return True
        return False