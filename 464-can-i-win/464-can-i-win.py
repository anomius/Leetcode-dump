class Solution:
    def canIWin(self, max_num: int, desiredTotal: int) -> bool:
        if desiredTotal<= max_num: return True
        
        if (max_num*(max_num+1)//2)< desiredTotal: return False
        
        mem ={}
        
        
        def dp(total, seen):
            if total>=desiredTotal: return False
            
            if (total,seen) in mem: return mem[(total,seen)]
            
            ans = False
            for num in range(1, max_num+1):
                if 1<<num & seen: continue
                
                new_seen= seen|1<<num
                temp= dp(total+num, new_seen)
                if not temp: 
                    mem[(total, seen)]= True
                    return True #i can force other player to lose by picking this
                
            mem[(total,seen)]= ans
            return ans
        
        return dp(0,0)