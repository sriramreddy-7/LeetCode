class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # c=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j] and i <j:
        #             c=c+1
        # return c
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=0
        for k,v in d.items():
            if v>=2:
                c=c+(v*(v-1)//2)
        return c