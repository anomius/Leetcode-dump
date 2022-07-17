class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = {}
        for i in range(2, n+1):
            for j in range(1, i):
                if i/j not in ans:
                    ans[i/j] = f'{j}/{i}'
        return ans.values()
        