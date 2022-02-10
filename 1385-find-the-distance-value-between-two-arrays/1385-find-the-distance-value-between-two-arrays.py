class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cout=0
        for i in arr1:
            cout+=1
            for j in arr2:
                if abs(i-j)<=d:
                    cout-=1
                    break
        
        return cout