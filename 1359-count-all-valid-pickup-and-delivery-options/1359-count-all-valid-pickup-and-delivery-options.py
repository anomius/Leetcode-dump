class Solution:
    def countOrders(self, n: int) -> int:
        mod=10**9 + 7
        dp=[]
        dp.append(0)
        dp.append(1)
        for i in range(2,n+1):
            dp.append((i*(2*i-1)*dp[i-1])%mod)
        return dp[n]
        