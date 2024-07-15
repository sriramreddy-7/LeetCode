class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                r=[]
                r.append(i)
                d[s[i]]=r
            else:
                e=d[s[i]]
                e.append(i)
                d[s[i]]=e
        mx=-1
        for k,v in d.items():
            if len(v)>=2 and (v[len(v)-1]-v[0])-1>mx:
                mx=(v[len(v)-1]-v[0])-1
        return mx