## 2 题解解法  回溯
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def trackback(nums,track):
            if len(track)==len(nums):
                res.append(track[:])
                return

            for i in nums:
                if i in track:
                    continue
                trackback(nums,track+[i])
        
        res = []
        trackback(nums,[])
        return res