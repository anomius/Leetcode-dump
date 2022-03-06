class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        pep=[0]*num_people
        g=1
        i=0
        while candies>g: 
            pep[i%num_people]+=g
            candies-=g
            g+=1
            i+=1
            
        pep[i%num_people]+=candies
        return pep
            