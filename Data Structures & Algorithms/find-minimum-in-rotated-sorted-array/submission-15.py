class Solution:
    def findMin(self, nums: List[int]) -> int:
        # I will use a binary search by setting a left, right, and middle pointer to list elements
        # we will determine if the left or the right side would likely contain the smaller element then reset
        # the pointers. We will stop when the left and right are pointing to the same position and we have 
        # our solution.

        # this is O(log n)

        left = 0
        right = len(nums) - 1

        if(nums[left] < nums[right]):
            return nums[left]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

            if(left == right):
                return nums[left]