class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        ht=[0]*(max(nums)+1)
        for i in nums:
            ht[i]=nums.count(i)
        r=[]
        c=0
        for j in range(len(ht)):
            if c<=3:
                if ht[j]>=1:
                    r.append(j)
                    c+=1
            if c==3:
                return r[1]
        else:
            return -1