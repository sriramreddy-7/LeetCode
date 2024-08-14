class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op=0
        for i in range(len(nums)):
            if nums[i]%3!=0:
                op+=1
        return op