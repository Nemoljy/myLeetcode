# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        lenth = len(num)
        if size>lenth:  ## 给nm恶心了，[10,14,12,11],5的正确输出是[]？？？怕不是出题者都错了
            return max(num)
        if size <= 0:
            return []
        res = []
        for i in range(lenth-size+1):
            res.append(max(num[i:i+size]))
        return res