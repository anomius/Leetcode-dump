class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        if total%3 == 0:
            return total

        rem1_min = [10000, 10000] # Smallest 2 numbers leaving remainder of 1
        rem2_min = [10000, 10000] # Smallest 2 numbers leaving remainder of 2
        for num in nums:
            if num % 3 == 1:
                if num < rem1_min[0]:
                    rem1_min[0], rem1_min[1] = num, rem1_min[0]
                elif num < rem1_min[1]:
                    rem1_min[1] = num
            elif num % 3 == 2:
                if num < rem2_min[0]:
                    rem2_min[0], rem2_min[1] = num, rem2_min[0]
                elif num < rem2_min[1]:
                    rem2_min[1] = num

        if total%3 == 1:
            return total - min(rem1_min[0], sum(rem2_min))
        if total%3 == 2:
            return total - min(rem2_min[0], sum(rem1_min))
