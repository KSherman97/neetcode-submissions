class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_string = "".join(char for char in s if char.isalnum()).lower()
        
        mid = int(len(temp_string) / 2)

        if(len(temp_string) % 2 == 0):
            first_half = sorted(temp_string[:mid])
            print(temp_string)
            second_half = sorted(temp_string[mid:])
        else:
            first_half = sorted(temp_string[:mid])
            print(temp_string)
            second_half = sorted(temp_string[mid+1:])
            
        print(f"{len(temp_string)}, {mid}")
        print(first_half)
        print(second_half)

        if first_half == second_half:
            return True

        return False