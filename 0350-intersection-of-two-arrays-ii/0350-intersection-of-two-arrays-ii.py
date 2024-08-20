class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r,d=[],{}
        count=0
        for i in nums1:
            if i not in d:
                r=[0]*2
                r[0]=1
                d[i]=r
            else:
                e=d[i]
                e[0]+=1
                d[i]=e

        for i in nums2:
            if i not in d:
                r=[0]*2
                r[1] = 1
                d[i] = r
            else:
                e = d[i]
                e[1] += 1
                d[i] = e

        r=[]
        for k,v in d.items():
            if v[1]==v[0]:
                r.extend([k]*v[1])
            else:
                r.extend([k]*min(v))
        return r