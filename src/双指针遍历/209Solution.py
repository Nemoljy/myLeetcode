## 209. 长度最小的子数组
#### 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#### https://leetcode-cn.com/problems/minimum-size-subarray-sum/

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums)<s:
            return 0
        l = 0
        r = 0
        mini = len(nums)+1
        while(r<len(nums)):
            r = r+1
            while(sum(nums[l:r])>=s):
                mini = min(mini,r-l)
                l=l+1
                        
        return mini
