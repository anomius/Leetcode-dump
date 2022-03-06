class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        rows = int((-1+(1+8*candies)**.5)/2/num_people)
        term0 = num_people*rows*(rows-1)//2
        ans = [rows*(i+1) + term0 for i in range(num_people)]
        excess = candies - sum(ans)

        i, pile = 0, rows*num_people+1
        while excess>0:
            ans[i]+= min(pile, excess)
            excess-= pile
            pile+= 1
            i+=1

        return ans