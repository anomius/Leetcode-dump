class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        zero_count = 0        
        z_projection = 0
        
        for i in grid:
            z_projection += max(i)
        
        y_projection = 0
        
        for j in range(len(grid[0])):
            max_n = -1
            
            for i in range(len(grid)):
                max_n = max(max_n, grid[i][j])
                
                if grid[i][j] == 0:
                    zero_count += 1
            
            y_projection += max_n
            
        x_projection = len(grid) * len(grid[0]) - zero_count
        
        return x_projection + y_projection + z_projection