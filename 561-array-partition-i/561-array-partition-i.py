class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num=sorted(nums)
        s=0
        for i in range(0,len(num),2):
            s+=num[i]
        return s
        