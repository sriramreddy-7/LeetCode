class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=[0]*2
        for k,v in d.items():
            if v%2==0:
                c[0]+=(v//2)
            else:
                c[0]+=(v-1)//2
                c[1]+=1
        return c