class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0]>target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return end