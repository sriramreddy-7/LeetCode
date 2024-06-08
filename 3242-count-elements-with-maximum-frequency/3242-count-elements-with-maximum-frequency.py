class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m=max(nums)
        m=m+1
        ht=[0]*m
        for i in nums:
            ht[i]=nums.count(i)
        mx=max(ht)
        c=ht.count(mx)
        return c*mx