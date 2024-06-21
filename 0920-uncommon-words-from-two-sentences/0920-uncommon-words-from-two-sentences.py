class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l=list(map(str,(s1+" "+s2).split(" ")))
        d={}
        for i in l:
            if  i not in d:
                d[i]=1
            else:
                d[i]+=1
        r=[]
        for k,v in d.items():
            if v==1:
                r.append(k)
        return r
