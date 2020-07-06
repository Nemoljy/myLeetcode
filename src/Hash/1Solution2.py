## 1. 两数之和
#### 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#### 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#### https://leetcode-cn.com/problems/two-sum/

## 字典 O(n)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            print(hashmap)
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
