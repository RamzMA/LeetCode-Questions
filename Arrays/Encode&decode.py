from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return strs
        
        joined = ""
        
        for word in strs:
            joined = joined + f"{len(word)}#{word}"

        return joined

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            words.append(s[i + 1: j + 1 + length])
            i = j+1+length
        return words
            

        
            
# Time Complexity: O(n) where n is the total number of characters in all the strings in the input list.
# Space Complexity: O(n) in the worst case when all strings are unique and stored in the output list.

#test cases
solution = Solution()
print(solution.encode(["Hello", "world"]))
print(solution.decode("5#Hello5"))
