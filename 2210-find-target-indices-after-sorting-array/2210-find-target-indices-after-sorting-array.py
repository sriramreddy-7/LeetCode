class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        r=[]
        for i in range(len(nums)):
            if nums[i]==target:
                r.append(i)
        return r
