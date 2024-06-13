class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)/2
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for k,v in d.items():
            if n==v:
                return k