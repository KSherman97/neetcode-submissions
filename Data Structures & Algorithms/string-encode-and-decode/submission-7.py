class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for string in strs:
            length = len(string)
            temp_string = str(length) + "#" + string
            final_string += temp_string
             
        return final_string

    def decode(self, s: str) -> List[str]:

        final_list = []
        counter = 0

        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])

            i = j+1
            final_list.append(s[i:i + length])

            i += length

        return final_list


