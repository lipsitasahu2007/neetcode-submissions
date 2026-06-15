class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=sorted(list(s))
        l1=sorted(list(t))
        if l==l1:
            return True
        return False
        
            
        