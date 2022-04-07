class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones=sorted(stones)
            k=abs(stones[-1]-stones[-2])
            stones.pop(-1)
            stones.pop(-1)    
            if k:
                stones.append(k)
        return stones[0] if stones else 0 
        