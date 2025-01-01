class Solution:
    def maxScore(self, s: str) -> int:
        _sum=0
        for i in range(1,len(s)):
            ls=list(map(int,s[:i]))
            rs=list(map(int,s[i:]))
            z,o=0,0
            for i in ls:
                if i==0:
                    z+=1
            for j in rs:
                if j==1:
                    o+=1
            cs=z+o
            _sum=max(_sum,cs)
        return _sum