class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        l=[]
        out=[]
        for i in range(2,n+1):
            for j in range(1,i):
                if j/i not in l:
                    l.append(j/i)
                    out.append(f"{j}/{i}")
        return out
        