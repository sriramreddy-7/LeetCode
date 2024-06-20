class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i not in  d:
                d[i]=1
            else:
                d[i]+=1

        t=[]
        for k,v in d.items():
            if v>=2:
                t.append(k)
        for i in range(1,len(nums)+1):
            if i not in nums:
                t.append(i)
        return t