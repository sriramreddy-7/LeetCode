class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d={}
        for i in word1:
            if i not in d:
                r=[0]*2
                r[0]+=1
                d[i]=r
            else:
                e=d[i]
                e[0]+=1
                d[i]=e
        for i in word2:
            if i not in d:
                r=[0]*2
                r[1]+=1
                d[i]=r
            else:
                e=d[i]
                e[1]+=1
                d[i]=e
        for k,v in d.items():
            if abs(v[0]-v[1])>3:
                return False
        else:
            return True
        