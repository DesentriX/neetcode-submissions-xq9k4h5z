class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c for c in s if c.isalnum())
        clean = clean.lower()
        rev = clean[::-1]
        return rev == clean
        
           
        
        
        

        