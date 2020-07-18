## 2 题解解法  回溯
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def trackback(used,track):
            if len(track)==len(nums):
                res.append(track[:])
                return

            for i in range(len(nums)):
                if used[i] or (i>0 and nums[i]==nums[i-1] and not used[i-1]):  ## 增加剪枝：该选项与上次相等，且上次没有被使用
                    continue
                used[i] = True
                trackback(used,track+[nums[i]])
                used[i] = False
        
        res = []
        nums.sort()
        used = [False]*len(nums)
        trackback(used,[])
        return res