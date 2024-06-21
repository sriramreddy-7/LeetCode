class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        d={}
        for i in nums:
            for j in i:
                if j not in d:
                    d[j]=1
                else:
                    d[j]+=1
        nums=[]
        for k,v in d.items():
            if v==n:
                nums.append(k)
        if nums!=[]:
            nums.sort()
            return nums
        return []