class Solution:
    def cutRope(self, number):
        ## 递归贪心计算
        def max_multi(n,m):
            return (n//m)*max_multi(n-n//m,m-1) if n%m != 0 else pow(n/m,m)

        res = 0
        for m in range(2,number//2+1):
            res = max(max_multi(number,m),res)
            
        return res