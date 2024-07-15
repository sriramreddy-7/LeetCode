class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def check(x,ca,k):
            if x<=k:
                ca.add(x)
            if len(ca)!=k:
                return True
            else:
                return False

        ca=set()

        def find():
            c = 0
            for i in range(len(nums)-1,-1,-1):
                if check(nums[i],ca,k):
                    c=c+1
                    continue
                else:
                    return c+1
        return find()