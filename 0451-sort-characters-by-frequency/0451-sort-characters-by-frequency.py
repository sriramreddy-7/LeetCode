class Solution:
    def frequencySort(self, s: str) -> str:
        l=set(s)
        d={}
        for i in l:
            c=s.count(i)
            if c not in d:
                r=[i]
                d[c]=r
            else:
                e=d[c]
                e.append(i)
                d[c]=e
            d[c].sort()

        s=""
        d=dict(sorted(d.items(),reverse=True))
        for k,v in d.items():
            for i in v:
                s=s+k*i
        return s