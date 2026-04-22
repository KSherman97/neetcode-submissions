class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_string = "".join(char for char in s if char.isalnum()).lower()
        
        mid = int(len(temp_string) / 2)

        if(len(temp_string) % 2 == 0):
            first_half = sorted(temp_string[:mid])
            second_half = sorted(temp_string[mid:])
        else:
            first_half = sorted(temp_string[:mid])
            second_half = sorted(temp_string[mid+1:])

        if first_half == second_half:
            return True

        return False