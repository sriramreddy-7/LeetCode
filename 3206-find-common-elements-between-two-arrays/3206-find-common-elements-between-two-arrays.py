class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1,c2=0,0
        def count(x,arr):
            if x in arr:
                return 1 
            else:
                return 0
        for i in nums1:
            c1+=count(i,nums2)
        for i in nums2:
            c2+=count(i,nums1)
        return [c1,c2]