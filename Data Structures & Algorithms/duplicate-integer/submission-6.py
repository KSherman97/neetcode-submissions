class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary.update({num: 1})
            else:
                return True

        return False