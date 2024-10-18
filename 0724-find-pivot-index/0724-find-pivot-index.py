class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ts=sum(nums)
        ls=0
        for i in range(len(nums)):
            rs=ts-ls-nums[i]
            if rs==ls:
                return i
            ls+=nums[i]
        else:
            return -1