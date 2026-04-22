class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we will need to use binary search
        # split in half by comparing the pivot to the mid point
        # repeat until the left and right pointer are the same position and this is our solution

        left, right = 0, len(nums) - 1

        # if the array size <= 3 then we can just return the index instead of doing a binary search
        if len(nums) <= 3:
            i = 0
            while i < len(nums):
                if(nums[i] == target):
                    return i
                i += 1
            return -1

        while left <= right:
            mid_point = (left+right) // 2

            if target == nums[mid_point]:
                return mid_point


            # if left < mid the pivot must be in the right
            # this is case number one where the left half is sorted
            if nums[left] <= nums[mid_point]:
                if nums[left] <= target < nums[mid_point]:
                    right = mid_point - 1
                else:
                    left = mid_point + 1
                
            # if the mid < right then the pivot must be in the left
            # this is case number two wher the right half is sorted
            else:
                if nums[mid_point] < target <= nums[right]:
                    left = mid_point+1
                else:
                    right = mid_point - 1

        return -1
        