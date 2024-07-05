class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d={}
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
                r[1]=1
                d[i]=r
            else:
                e=d[i]
                e[1]+=1
                d[i]=e
        s1=[]
        s2=[]
        for k,v in d.items():
            if v[0]>=1 and v[1]==0:
                s1.append(k)
            if v[0]==0 and v[1]>=1:
                s2.append(k)
        return [s1,s2]