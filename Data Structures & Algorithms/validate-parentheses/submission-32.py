class Solution:
    def isValid(self, s: str) -> bool:

        # we can optimize this solution by utilizing a hasmap to compare characters with their closing pair
        # this solution is O(n) complexity because it will only itterate through the string a single time at most
        # append and pop to a list and dict lookups are all constant time operations O(1)
        stack = []
        char_map = {"}":"{", ")":"(", "]":"["}

        if len(s) % 2 == 1:
            return False
        
        for char in s:
            if char in char_map:
                top_char = ""
                if len(stack) > 0:
                    top_char = stack.pop()

                if char_map[char] != top_char:
                    return False

            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        return False