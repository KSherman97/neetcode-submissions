class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_string = "".join(char for char in s if char.isalnum()).lower()

        left = 0
        right = len(temp_string) - 1

        while left < right:
            if temp_string[left] != temp_string[right]:
                return False
            left += 1
            right -= 1

        return True