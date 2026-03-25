class Solution(object):
    def isPalindrome(self, s):
        
        
        cleaned = ''.join(c.lower() for c in s if c.isalpha()) 

        left,right = 0, len(cleaned) - 1

        while left != right:
            if cleaned[left] != cleaned[right]:
                return False

            left += 1
            right -= 1

        return True

#Test Cases
solution = Solution()
print(solution.isPalindrome("car")) # returns false as car is not a palindrome
print(solution.isPalindrome("wow")) # returns true as wow is a palindrome
print(solution.isPalindrome("A man, a plan, a canal: Panama")) # returns true as it is a palindrome
print(solution.isPalindrome("race a car")) # returns false as race a car is not a palindrome

