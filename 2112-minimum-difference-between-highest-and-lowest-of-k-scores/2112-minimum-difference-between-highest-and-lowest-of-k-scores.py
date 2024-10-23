class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        seen=set()
        for i in range(len(nums)-1):
            if len(nums[i:i+k])==k:
                x=nums[i:i+k]
                seen.add(abs(min(x)-max(x)))
        if seen:
            return min(seen)
        return 0