class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l=0
        r=len(s)-1
        
        while l<r:
            if s[l].isalpha() and s[r].isalpha():
                if s[l].lower() == s[r].lower():
                    l+=1
                    r-=1
                else:
                    return False
            
            while l<r and not s[l].isalpha():
                l+=1
            while l<r and not s[r].isalpha():
                r-=1
        return True