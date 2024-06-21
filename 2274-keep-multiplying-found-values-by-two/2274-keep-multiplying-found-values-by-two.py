class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        def find(key):
            if original in nums:
                return 2*original
            else:
                return False

        for i in range(len(nums)+1):
            r=find(original)
            if r!=False:
                original=r
            else:
                return original