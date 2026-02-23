#we assume that it will all be lowercase as stated in thw question
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hsS,hsT = {}, {}

        for i in range(len(s)):
            hsS[s[i]] = hsS.get(s[i], 0) + 1
            hsT[t[i]] = hsT.get(t[i], 0) + 1

        return hsS == hsT
    
# Time Complexity: O(n) where n is the length of the input strings.
# Space Complexity: O(1) since the hash maps will contain at most 26 keys

#test cases
solution = Solution()
print(solution.isAnagram("racecar","carrace")) # Output: True (both strings have the same characters with the same frequency)
print(solution.isAnagram("hello","world")) # Output: False (different characters and frequencies)
print(solution.isAnagram("anagram","nagaram")) # Output: True (both strings have the same characters with the same frequency)
print(solution.isAnagram("rat","car")) # Output: False (different characters and frequencies)
print(solution.isAnagram("listen","silent")) # Output: True (both strings have the same characters with the same frequency)