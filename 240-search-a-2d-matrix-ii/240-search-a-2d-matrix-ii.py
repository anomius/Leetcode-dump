class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l =0
            r = len(i)
            while l<r:
                mid = (l+r)//2
                if i[mid] > target:
                    r-=1
                elif i[mid]<target:
                    l+=1
                else:
                    return True
        return False