# -*- coding:utf-8 -*-
class Solution:
    def dfs(self,row,col,track):
        if self.flag:  ## 找到了直接不管了
            return
        if self.target == track:  ## 顺序有关系，如果这个在下面的if后面，那么1x1的矩阵无法判断True
            self.flag = True
            return
        if not (row>=0 and row<self.rows and col>=0 and col<self.cols):  ## 越界
            return
        if self._moved.get((row,col)):  ## 去过了
            return
        
        if self.matrix[row][col] == self.target[len(track)]:
            
            track += self.matrix[row][col]
            self._moved[(row,col)] = True

            self.dfs(row+1,col,track)
            self.dfs(row-1,col,track)
            self.dfs(row,col+1,track)
            self.dfs(row,col-1,track)
        
        return
    
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        self.matrix = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]  ## tmd输入竟然是个字符串……
        self.rows, self.cols, self.target = rows, cols, path
        self.flag = False

        for i in range(rows):
            for j in range(cols):
                if self.matrix[i][j] == path[0]:
                    self._moved = {}
                    self.dfs(i,j,'')

        return self.flag