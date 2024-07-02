class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        r=[]
        for k,v in d.items():
            if v==2:
                r.append(k)
        return r