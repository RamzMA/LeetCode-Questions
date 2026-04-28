from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        Set a hs with defaultdict to initialise a empty dict to allow for appending, then loop through all words in strs.
        Sort each word and check for the position of sorted in hs and append word to position of sorted word. 
        This ensures all words when sorted that are the same are grouped together.

        Time complexity: O(n * k log k)
        Space complexity: O(n)
        """

        hs = defaultdict(list)

        for word in strs:
            sortWord = "".join(sorted(word))
            hs[sortWord].append(word)

        return list(hs.values())


# test cases
solution = Solution()
print(
    solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
)  # [['eat','tea','ate'],['tan','nat'],['bat']]
print(solution.groupAnagrams([""]))  # [['']]
print(solution.groupAnagrams(["a"]))  # [['a']]
print(
    solution.groupAnagrams(["abc", "bca", "cab", "xyz", "zyx"])
)  # [['abc','bca','cab'],['xyz','zyx']]

