class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        if nums==[]:
            return -1
        d={}
        for i in nums:
            if -i in nums:
                d[i]=-i
        if d!={}:
            return max(d)
        else:
            return -1
