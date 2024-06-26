class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count=0
        d={}
        for i in words1:
            if i not in d:
                r=[0]*2
                r[0]=1
                d[i]=r
            else:
                e=d[i]
                e[0]+=1
                d[i]=e

        for i in words2:
            if i not in d:
                r=[0]*2
                r[1] = 1
                d[i] = r
            else:
                e = d[i]
                e[1] += 1
                d[i] = e

        c=0
        for k,v in d.items():
            if v[0]==1 and v[1]==1:
                count+=1
        return count