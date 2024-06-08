class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in arr:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        c=1
        for key,v in d.items():
            if v==1:
                if c==k:
                    return key
                else:
                    c=c+1
        return ""
            