class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if nums is None or len(nums) == 0:
            return res
        size = len(nums)
        l, r = 0, size - 1
        while l < r:
            m = (l + r)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[r] != target:
            return res
        res[0] = r
        l, r = 0, size
        while l < r:
            m = (l + r)//2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        res[1] = l - 1
        return res    
