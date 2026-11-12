# python basics
# In an inner function, reading an outer variable works, 
# and so does mutating an outer object (lst[0] = x, 
# lst.append(x)), but assigning to a name (x = ..., x += 1)
# creates a new local variable instead of updating the outer 
# one, which causes UnboundLocalError if you read it first; 
# to rebind an outer variable, declare it with nonlocal, or 
# store the state in a mutable container like a list and 
# mutate that.

# In Python, many functions compare items, and by default they compare the items themselves, but the key= parameter lets you pass any one-argument function (a built-in like len, your own def, or a lambda, eg. lambda x: x[0], etc.) that is called on each item so the comparison is done on its return value instead, while the result still contains the original items rather than the key values. It works the same way in max, min, sorted, list.sort, heapq.nlargest/nsmallest/merge, itertools.groupby ... 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # def find(l, r):



        
        
        
        # two pointers
        START_IDX = 0
        MAX_LEN = 0
    
        def find_longest(l, r) -> tuple:
            nonlocal START_IDX, MAX_LEN
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > MAX_LEN:
                    START_IDX = l
                    MAX_LEN = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd number
            find_longest(i, i)
            # even number 
            find_longest(i, i+1)
        
        return s[START_IDX : START_IDX + MAX_LEN]

        
        
        