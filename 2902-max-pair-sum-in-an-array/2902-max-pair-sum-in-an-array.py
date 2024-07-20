class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            r=[int(_) for _ in str(nums[i])]
            rmax=max(r)
            if rmax not in d:
                e=[]
                e.append(nums[i])
                d[rmax]=e
            else:
                e=d[rmax]
                e.append(nums[i])
                d[rmax]=e

        final=set()
        for k,v in d.items():
            v.sort()
            if len(v)>2:
                final.add(v[-1]+v[-2])
            elif len(v)==2:
                final.add(v[0] + v[1])
        if final:
            return max(final)
        return -1