class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        c=0
        start=0
        end=len(nums)-1
        while start<=end:
            if nums[start]+nums[end]<target:
                c+=end-start
                start+=1
            else:
                end-=1
        return c