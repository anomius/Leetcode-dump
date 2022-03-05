class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        m=10**4
        dp={i:0 for i in range(0,m+2)}
        if 1 in d:
            dp[1]=d[1]
        else: 
            dp[1]=0
        for i in range(2,m+2):
            if i in d:
                dp[i]=max(i*d[i]+dp[i-2],dp[i-1])
            else:
                dp[i]=dp[i-1]    
        return dp[m]
        
        