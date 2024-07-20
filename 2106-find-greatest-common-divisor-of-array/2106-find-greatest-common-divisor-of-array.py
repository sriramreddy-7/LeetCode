class Solution:
    def findGCD(self, nums: List[int]) -> int:
        _min=min(nums)
        _max=max(nums)
        for i in range(_min,0,-1):
            if _min%i==0 and _max%i==0:
                return i