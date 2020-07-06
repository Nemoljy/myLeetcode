## 1. 两数之和
#### 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#### 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#### https://leetcode-cn.com/problems/two-sum/

## 傻瓜遍历 O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
             
        for i,n in enumerate(nums):
            for j in range(i+1,len(nums)):
                if n+nums[j]==target:
                    return i,j
