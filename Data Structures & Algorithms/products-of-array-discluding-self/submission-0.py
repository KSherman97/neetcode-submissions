class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # loop through each item in the nums array and multiply it by every other item
        final_list = []

        for i in range(len(nums)):
            counter = 1
            for j in range(len(nums)):
                if j != i:
                    counter = counter * nums[j]
            final_list.append(counter)

        return final_list