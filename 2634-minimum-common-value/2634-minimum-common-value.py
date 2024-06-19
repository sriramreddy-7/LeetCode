class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1=set(nums1)
        nums2=set(nums2)
        nums1=nums1.intersection(nums2)
        nums1=list(nums1)
        nums1.sort()
        if nums1:
            return nums1[0]
        else:
            return -1
