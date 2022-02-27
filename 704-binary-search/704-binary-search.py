class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def se(nums,left,right,target):
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif right<=left:
                return -1
            elif nums[mid]>target:
                return se(nums,left,mid-1,target)
            elif nums[mid]<target:
                return se(nums,mid+1,right,target)
        return se(nums,0,len(nums)-1,target)         
            