class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r=[]
        d={}
        count=0
        for i in s:
            if i not in d:
                r=[0]*2
                r[0]=1
                d[i]=r
            else:
                e=d[i]
                e[0]+=1
                d[i]=e

        for i in t:
            if i not in d:
                r=[0]*2
                r[1] = 1
                d[i] = r
            else:
                e = d[i]
                e[1] += 1
                d[i] = e

        r=""
        for k,v in d.items():
            if v[1]!=v[0]:
                r=r+k
        return r