class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        out=[]
        for i in range(2,n+1):
            for j in range(1,i):
                if gcd(j, i) == 1:
                    out.append(f"{j}/{i}")
        return out
        