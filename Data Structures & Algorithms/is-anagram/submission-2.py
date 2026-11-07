class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)

        if len(s) != len(t):
            return False
            
        for k,v in s.items():
            if t[k] != v:
                return False
                
        return True