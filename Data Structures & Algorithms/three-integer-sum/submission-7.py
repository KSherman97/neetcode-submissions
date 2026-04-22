class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # set a pivot point, then a left and right pointer for n^2 solution
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            if a > 0:
                break

            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    
                    results.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1 

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return results