class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        s=set()
        while nums!=[]:
            a=min(nums)
            b=max(nums)
            avg=(a+b)/2
            s.add(avg)
            nums.remove(a)
            nums.remove(b)
        return len(s)