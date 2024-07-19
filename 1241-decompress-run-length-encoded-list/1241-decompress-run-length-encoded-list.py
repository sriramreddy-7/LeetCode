class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        s,f=0,1
        r=[]
        for i in range(len(nums)//2):
            r.extend([nums[f]]*nums[s])
            s+=2
            f+=2
        return r
        