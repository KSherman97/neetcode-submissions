class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        substring = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # slide the window smaller until there are no duplucates
            while s[right] in substring:
                substring.remove(s[left])
                left += 1

            # add the current character to hte substiring
            substring.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len