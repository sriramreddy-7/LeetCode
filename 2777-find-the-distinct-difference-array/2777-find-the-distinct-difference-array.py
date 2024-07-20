class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff=[]
        for i in range(len(nums)):
            s1=set(nums[:i+1])
            s2=set(nums[i+1:])
            diff.append(len(s1)-len(s2))
        return diff