class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set(nums)
        s=list(s)
        s.sort()
        if len(s)>=3:
            return s[-3]
        else:
            return s[-1]