class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        m, n = r-1, 0
        
        while m >= 0 and n < c: 
            if matrix[m][n] > target:
                m -= 1
            elif matrix[m][n] < target:
                n += 1
            else:
                return True
        return False