class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # string only consists of uppercase chars and int k
        # select up to k chars of the string to replace with any other char

        # perform at most k replacements to create the longest contiguous string of repeating chars

        # probably start with two pointers pointer for each sub string
        # one pointer will stay at the first char and the second will move until it hits a char that is different
        # that string will now be placed into an array indicating the starting and ending point
        # the longest item in that array 

        count = {}
        max_length = 0
        max_frequency = 0

        left = 0

        for right in range(len(s)):
            # first update the count for the new char
            count[s[right]] = 1 + count.get(s[right], 0)

            # keep track of most common char in the window
            max_frequency = max(max_frequency, count[s[right]])

            # check if the current window is vaid
            # window len is (right - left + 1)
            # if len - max_frequency > k then there are too many chars to replace relative to the defined k value
            while(right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length