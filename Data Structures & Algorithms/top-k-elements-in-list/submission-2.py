class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # itterate over the list and create a hashmap of the identifier and the count
        # order the hashmap by the count
        count_map = {}
        for num in nums:
            if num not in count_map:
                count = 1
            else:
                count = count_map[num] + 1
            
            count_map[num] = count

        final_list = list(sorted(count_map.items(), key=lambda item: item[1], reverse=True))
        final_list = final_list[0:k]

        return [x[0] for x in final_list]