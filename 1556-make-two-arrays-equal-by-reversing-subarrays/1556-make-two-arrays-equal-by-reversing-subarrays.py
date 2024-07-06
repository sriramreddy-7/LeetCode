class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d={}
        for i in target:
            if i not in d:
                r=[0]*2
                r[0]=1
                d[i]=r
            else:
                e=d[i]
                e[0]+=1
                d[i]=e
        for i in arr:
            if i not in d:
                r=[0]*2
                r[1]=1
                d[i]=r
            else:
                e=d[i]
                e[1]+=1
                d[i]=e
        for k,v in d.items():
            if v[0]!=v[1]:
                return False
        else:
            return True