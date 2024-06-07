class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        f=0
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                f=1
                return mid
            elif target<nums[mid]:
                j=mid-1
            else:
                i=mid+1
        if f==0:
            return -1