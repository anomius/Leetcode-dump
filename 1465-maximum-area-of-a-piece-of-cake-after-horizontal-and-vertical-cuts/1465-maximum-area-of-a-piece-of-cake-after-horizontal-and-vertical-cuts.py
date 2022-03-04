class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:   
        mod=10**9 + 7
        
        low=0
        hlist=[]
        vlist=[]
        horizontalCuts=sorted(horizontalCuts)
        verticalCuts=sorted(verticalCuts)
        for i in range(len(horizontalCuts)):
            hlist.append(horizontalCuts[i]-low)        
            low=horizontalCuts[i]
        hlist.append(h-low)
        low=0
        for i in range(len(verticalCuts)):
            vlist.append(verticalCuts[i]-low)        
            low=verticalCuts[i] 
        vlist.append(w-low)
        
        return max(hlist)*max(vlist)%mod