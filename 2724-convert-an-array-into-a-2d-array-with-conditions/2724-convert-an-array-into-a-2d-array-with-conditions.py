class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d={}
        if nums==list(set(nums)):
            return [nums]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        f=[]
        n=len(nums)
        while n:
            r=[]
            for k,v in d.items():
                if v!=0:
                    r.append(k)
                    d[k]=v-1
                    n-=1
            f.append(r)
        return f