## 思路  n个位置放右括号，n长的list，条件：pos[i]<=i+1且sum(pos)=n
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(n,pos):  ## 回溯法获得右括号的排列pos
            if len(pos)==n:
                if sum(pos)==n:
                    pos_res.append(pos[:])
                return
            for i in range(n+1):
                if i+sum(pos) > len(pos)+1 or i+sum(pos)>n:
                    continue
                pos.append(i)
                backtrack(n,pos)
                pos.pop(-1)
            return

        pos_res = []
        backtrack(n,[])

        res = []
        for p in pos_res:
            res.append(''.join(['('+')'*nums for nums in p]))
        return res
    