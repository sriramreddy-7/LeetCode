class Solution:
    def sortSentence(self, s: str) -> str:
        l=list(map(str,s.split(" ")))
        d=[0]*(len(l)+1)
        for i in l:
            if i not in d:
                k=int(i[-1])
                i=i.replace(str(k),"")
                d[k]=i
        d.remove(0)
        r=" ".join(d)
        return r