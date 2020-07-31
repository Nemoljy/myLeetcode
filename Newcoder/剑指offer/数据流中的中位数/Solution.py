# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        ## 这里插入排序
        self.data.append(num)
        i = len(self.data)-2
        
        while i>=0 and num<self.data[i]:
            self.data[i+1] = self.data[i]
            i -= 1
        self.data[i+1] = num
        
    def GetMedian(self):
        if len(self.data)%2:
            return self.data[len(self.data)//2]
        else:
            a = len(self.data)//2
            return (self.data[a-1]+self.data[a])/2