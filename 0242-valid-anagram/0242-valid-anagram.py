class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        l=[_ for _ in s]
        m=[_ for _ in t]
        l.sort()
        m.sort()
        if l!=m:
            return False
        else:
            return True


        