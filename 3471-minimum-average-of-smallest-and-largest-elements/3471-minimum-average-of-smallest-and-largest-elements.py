class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        d={}
        j=len(nums)-1
        averages=[]
        i=0
        while i<=j:
            averages.append((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return min(averages)