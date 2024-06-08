class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        x=0
        l=[0]*len(d)
        for k,v in d.items():
            l[x]=d[k]
            x=x+1
        for c in range(len(l)-1):
            if l[c]!=l[c+1]:
                return False
        else:
            return True