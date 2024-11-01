class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if all(nums)==False:
            return 0
        else:
            p=1
            for i in nums:
                p=p*i
            if p<0:
                return -1
            else:
                return 1
            
        