class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        pep=[0]*num_people
        g=1
        while candies>g: 
            pep[g%num_people-1]+=g
            candies-=g
            g+=1
        pep[g%num_people-1]+=candies
        return pep
            