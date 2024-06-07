class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid=(len(nums))//2
        n1=nums[:mid]
        n2=nums[mid:]
        nums=[]
        for i in range(len(n1)):
            nums.append(n1[i])
            nums.append(n2[i])
        return nums
        