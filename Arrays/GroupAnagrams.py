from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0 or len(strs) == 1:
            return strs
        
        seen = {}

        for word in strs:
            sort = "".join(sorted(word))
            if sort not in seen:
                seen[sort] = []
            seen[sort].append(word)

        return list(seen.values())
    

# Time Complexity: O(n * k log k) where n is the number of strings in the input list and k is the maximum length of a string.
# Space Complexity: O(n * k) in the worst case when all strings are anagrams of each other and stored in the hash map.
solution = Solution()
print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))
print(solution.groupAnagrams(["abc","bca","cab","xyz","zyx"]))