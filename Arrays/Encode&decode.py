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
            while j < len(s) and s[j] != '#':
                j += 1
            if j == len(s):
                # '#' not found
                break
            length = int(s[i:j])
            words.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return words
            

        
            
# Time Complexity: O(n) where n is the total number of characters in all the strings in the input list.
# Space Complexity: O(n) in the worst case when all strings are unique and stored in the output list.

#test cases
solution = Solution()
encoded = solution.encode(["Hello", "world"])
print(encoded)
print(solution.decode(encoded))
