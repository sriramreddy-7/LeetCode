class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        i=0
        while i<2:
            for j in range(len(nums)):
                ans.append(nums[j])
            i=i+1
        return ans
