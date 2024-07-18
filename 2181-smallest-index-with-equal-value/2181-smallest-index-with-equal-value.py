class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        t=set()
        for i in range(len(nums)):
            if i%10==nums[i]:
                t.add(i)
        if t:
            return min(t)
        return -1