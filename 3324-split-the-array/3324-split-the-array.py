class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        r1=[]
        r2=[]
        for k,v in d.items():
            if v>2:
                return False
            else:
                if v==1:
                    if len(r1)<len(r2):
                        r1.append(k)
                    else:
                        r2.append(k)
                elif v==2:
                    r1.append(k)
                    r2.append(k)
        if len(r1)==len(r2):
            return True
        return False