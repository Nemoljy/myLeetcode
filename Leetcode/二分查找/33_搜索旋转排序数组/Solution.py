class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = int((end+start)/2)
            if nums[mid] == target:
                return mid
            ## 如果左边有序
            if nums[start] < nums[mid]:
                if nums[start] <= target and target <= nums[mid]:  ##且tar在左边
                    end = mid
                else:  ## 说明tar在右边
                    start = mid
            ## 如果右边有序
            elif nums[mid] < nums[end]:
                if nums[mid] <= target and target <= nums[end]: 
                    start = mid
                else:
                    end = mid
            
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1