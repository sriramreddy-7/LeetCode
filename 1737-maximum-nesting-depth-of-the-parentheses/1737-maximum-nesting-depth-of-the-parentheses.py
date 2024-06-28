class Solution:
    def maxDepth(self, s: str) -> int:
        r=[]
        c=0
        for i in s:
            if i=="(":
                c=c+1
            elif i==")":
                c=c-1
            r.append(c) 
        return max(r)