import re

def isPalindrome(s, l=0, r=None):
    if r is None: # limiting the text cleaning process for one time execution
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        r = len(s)-1
    
    if l >= r: # base case (pointers are passing then string is palindrome)
        return True
    
    if s[l] != s[r]:
        return False
    return isPalindrome(s, l+1, r-1) # Recursive call

## Another approach: Iterative 
# same text cleaning will be done except at last a normal check for same string
# Both have same TC O(n)

def chkpal(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return s == s[::-1] 