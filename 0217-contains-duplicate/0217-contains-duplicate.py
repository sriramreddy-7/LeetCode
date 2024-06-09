class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s1=len(nums)
        s2=len(set(nums))
        if s1==s2:
            return False
        else:
            return True