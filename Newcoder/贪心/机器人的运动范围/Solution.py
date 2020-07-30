# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = 0
        self.moved = {}
        
    def get_sum(self, n):
        sum = 0
        while n:
            sum += n%10
            n = n//10
        return sum
    
    def move(self, row,col):
        if not(row>=0 and row<self.rows and col>=0 and col<self.cols):  ## 越界
            return
        if self.get_sum(row)+self.get_sum(col)>self.threshold:  ## 条件k
            return
        if self.moved.get((row,col)) == 1: ## 用字典确定是否去过，知识点啊这个key的格式
            return

        self.moved[(row,col)] = 1
        self.res += 1
        
        self.move(row+1,col)
        self.move(row-1,col)
        self.move(row,col+1)
        self.move(row,col-1)
        return
    
    def movingCount(self, threshold, rows, cols):
        self.threshold = threshold
        self.rows = rows
        self.cols = cols
        self.move(0,0)
        return self.res