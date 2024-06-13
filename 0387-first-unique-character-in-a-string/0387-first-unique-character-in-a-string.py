class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                d[s[i]]=-1
        for k,v in d.items():
            if v!=-1:
                return v
        else:
            return -1