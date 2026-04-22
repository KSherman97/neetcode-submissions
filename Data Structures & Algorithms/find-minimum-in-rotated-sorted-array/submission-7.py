class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mid_point = int(len(nums) / 2)

        print(f"{l} {r} {mid_point}")

        if(len(nums) < 3):
            return min(nums)

        if nums[r] < nums[mid_point]:
            return min(nums[mid_point:r+1])
        else:
            return min(nums[l:mid_point+1])