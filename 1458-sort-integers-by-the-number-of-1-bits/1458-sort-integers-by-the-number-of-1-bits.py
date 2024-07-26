class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d={}
        for i in arr:
            r=str(bin(i))[2:]
            c=r.count("1")
            if c not in d:
                e=[]
                e.append(i)
                d[c]=e
            else:
                x=d[c]
                x.append(i)
                d[c]=x
        dic=dict(sorted(d.items()))
        result=[]
        for k,v in dic.items():
            v.sort()
            result.extend(v)
        return result