class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

        for k,v in d.items():
            if v%2!=0:
                return False
        else:
            return True