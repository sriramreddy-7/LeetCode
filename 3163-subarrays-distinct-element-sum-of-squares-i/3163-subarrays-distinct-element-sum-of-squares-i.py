class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        r=[]
        for i in range(1,len(nums)+1):
            for j in range(len(nums)):
                x=0
                if i==len(nums[j:j+i]):
                    x=len(set(nums[j:j+i]))
                    r.append(x*x)
        return sum(r)