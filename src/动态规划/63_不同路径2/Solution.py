##动态规划 DP   时间空间都是O(nm)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ## 第一格就有障碍物是我没想到的
        if obstacleGrid[0][0]==1:
            return 0
         
        m = len(obstacleGrid) ## m行
        n = len(obstacleGrid[0])  ## n列
        
        #初始化第一列和第一行
        grid = [[0]*n for i in range(m)]
        for i in range(m):  #初始化第一列
            if obstacleGrid[i][0]==1:
                break
            grid[i][0] = 1
        for j in range(n):  #初始化第一行
            if obstacleGrid[0][j]==1:
                break
            grid[0][j] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    grid[i][j] = grid[i-1][j]+grid[i][j-1]
        return grid[m-1][n-1]
