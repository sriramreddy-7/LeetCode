class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = {}
        for i in range(len(nums)-1):
            if nums[i]==key:
                if nums[i+1] not in d:
                    d[nums[i+1]]=1
                else:
                    d[nums[i+1]]+=1
        mxe=-1
        ky=0
        for k,v in d.items():
            if v>mxe:
                ky=k
                mxe=v
        return ky