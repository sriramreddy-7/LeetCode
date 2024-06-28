class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        mx=-1
        for k,v in d.items():
            if k==v and k>mx:
                mx=k
        return mx