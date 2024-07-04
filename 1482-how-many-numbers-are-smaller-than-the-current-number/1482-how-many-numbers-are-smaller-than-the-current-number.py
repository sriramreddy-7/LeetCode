class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if j!=i and nums[j]<nums[i]:
                    c=c+1
            r.append(c)
        return r