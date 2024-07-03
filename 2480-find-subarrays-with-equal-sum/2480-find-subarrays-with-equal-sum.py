class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s=set()
        for i in range(len(nums)):
            sub_array=nums[i:i+2]
            if len(sub_array)==2:
                _sum=sub_array[0]+sub_array[1]
                if _sum not in s:
                    s.add(_sum)
                else:
                    return True
        else:
            return False