class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        mx=-1
        value=set()
        for k,v in d.items():
            if k%2==0 and v>mx:
                value=set()
                value.add(k)
                mx=v
            elif k%2==0 and v==mx:
                value.add(k)
        if value:
            return min(value)
        else:
            return -1

        