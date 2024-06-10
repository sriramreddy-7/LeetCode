class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        n=len(arr)
        n=0.25*n
        for k,v in d.items():
            if v>n:
                return k