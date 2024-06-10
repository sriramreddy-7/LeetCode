class Solution:
    def averageValue(self, nums: List[int]) -> int:
        avg=[]
        for i in nums:
            if i%2==0 and i%3==0:
                avg.append(i)
        if avg!=[]:
            return int(sum(avg)/len(avg))
        return 0