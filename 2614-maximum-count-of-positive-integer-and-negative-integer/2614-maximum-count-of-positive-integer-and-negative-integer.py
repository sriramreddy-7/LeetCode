class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p=0
        n=0
        for i in nums:
            if i<0:
                n=n+1
            else:
                if i>0:
                    p=p+1
        if p>n:
            return p
        else:
            return n