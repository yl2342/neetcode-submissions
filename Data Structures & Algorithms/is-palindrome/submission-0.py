class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True 

        l, r = 0, len(s)-1

        # if the alphanum character num is odd that is fine-> Palindrome, when r = l
        while l < r:
            # pass special characters unitil next alphanum character
            while l < r and not self.isAlphanum(s[l]):
                l += 1
            while l < r and not self.isAlphanum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l+1, r-1

        return True
    
    def isAlphanum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))

            
        