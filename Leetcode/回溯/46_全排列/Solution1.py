## 法1 插值
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def getit(nums,tmp):
            if not nums:
                return []

            n = nums.pop(0)
            tmp = getit(nums,tmp) if len(nums)>1 else [nums]
            result = []
            for l in tmp:
                for i in range(len(l)+1):
                    result.append(l[:i]+[n]+l[i:])
            return result

        res = []
        return getit(nums,res)