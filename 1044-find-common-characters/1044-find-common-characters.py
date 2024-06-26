class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l=[_ for _ in min(words)]
        d={}
        def dic(c,j,i):
            if j not in d:
                r=[0]*len(words)
                r[i]=c
                d[j]=r
            else:
                e=d[j]
                e[i]=c
                d[j]=e

        for i in range(len(words)):
            for j in l:
                c=words[i].count(j)
                dic(c,j,i)

        r=[]
        def final(k,v):
            for i in range(min(v)):
                r.append(k)

        for k,v in d.items():
            if all(v):
                final(k,v)
        
        return r