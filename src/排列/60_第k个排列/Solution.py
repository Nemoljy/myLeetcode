## 脑抽写出来的分组写法，边界条件很多导致错4次，但速度很快  12 ms, 在所有 Python 提交中击败了97.89%的用户
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(n):
            return (n*factorial(n-1)) if n != 0 else 1
        
        ind = []
        ori_n = n
        b = k
        n_list = list(range(1,n+1))
        while b!=0 and b!=1:
            a = b // factorial(n-1)
            b = b % factorial(n-1)
            ind.append(a)
            n -= 1
        if b==1:
            ind += [0]*n
        else:
            ind[-1] = ind[-1]-1
            ind += [-1]*n
        print(ind)
        
        result = ''
        for i in ind:
            result = result+str(n_list.pop(i))
        
        return result
        