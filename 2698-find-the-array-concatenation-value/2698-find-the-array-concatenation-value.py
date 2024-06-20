class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        def add(a,b):
            r=int(str(a)+str(b))
            return r

        f=[]
        while nums!=[]:
            a,b=nums[0],nums[-1]
            if nums.index(a)!=nums.index(b) or len(nums)>2:
                nums.pop(0)
                nums.pop(-1)
                f.append(add(a, b))
            elif nums.index(a)==nums.index(b) and len(nums)==2:
                nums.pop(0)
                nums.pop(-1)
                f.append(add(a, b))
            else :
                if len(nums)<=1:
                    f.append(a)
                    nums.pop(0)

        return sum(f)