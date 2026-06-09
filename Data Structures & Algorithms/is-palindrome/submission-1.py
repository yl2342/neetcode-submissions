class Solution:
    @staticmethod
    def isAlphanum(c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))

    # --- Instance Method ---
    # - Defined with 'self' as the first parameter
    # - Has access to instance attributes (self.name, self.age, etc.)
    # - Most common type, used for behavior tied to a specific object
    # - Called on an instance: obj.method()

    # --- Static Method (@staticmethod) ---
    # - No 'self' or 'cls' parameter
    # - Cannot access instance or class attributes
    # - Just a regular function namespaced inside a class
    # - Use when logic is related to the class but doesn't need any class/instance data
    # - Called on class or instance: MyClass.method() or obj.method()

    # --- Class Method (@classmethod) ---
    # - Defined with 'cls' as the first parameter (refers to the class itself)
    # - Can access and modify class-level attributes (shared across all instances)
    # - Commonly used as alternative constructors (e.g. create object from different input)
    # - Called on class or instance: MyClass.method() or obj.method()

    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True 

        l, r = 0, len(s)-1

        # if the alphanum character num is odd that is fine-> Palindrome, when r = l
        while l < r:
            # pass special characters unitil next alphanum character
            while l < r and not Solution.isAlphanum(s[l]):
                l += 1
            while l < r and not Solution.isAlphanum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l+1, r-1

        return True
    
    

            
        