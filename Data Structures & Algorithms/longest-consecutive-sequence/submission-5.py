class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = {}
        counter = 0

        for num in nums:
            num_map[num] = 1

        for num in num_map.keys():
            if num-1 in num_map.keys():
                continue
            current = 1
            while num + 1 in num_map.keys():
                current += 1
                num += 1
            
            counter = max(current, counter)

        return counter