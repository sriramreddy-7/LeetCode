class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def red(x,nums):
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i]=nums[i]-x
            return nums
        def find_min(nums):
            x=101
            for i in nums:
                if i!=0 and i<x:
                    x=i
            return x
        def check(nums):
            c=0
            for i in range(len(nums)):
                if any(nums)==False:
                    return c
                x=find_min(nums)
                nums=red(x,nums)
                c=c+1
                if any(nums):
                    continue
                else:
                    return c
        return check(nums)