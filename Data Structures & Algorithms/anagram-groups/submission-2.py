class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_map = {}

        for item in strs:
            key = "".join(sorted(item))

            if key not in final_map:
                final_map[key] = []
            
            final_map[key].append(item)

        # sort the entire list in alphabetical order
        # append matches to the final list
        return list(final_map.values())