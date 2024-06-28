class Solution:
    def maxDepth(self, s: str) -> int:
        r=[]
        c=0
        for i in s:
            if i=="(":
                r.append(c)
                c=0
            elif i==")":
                c=c+1 
        return c 