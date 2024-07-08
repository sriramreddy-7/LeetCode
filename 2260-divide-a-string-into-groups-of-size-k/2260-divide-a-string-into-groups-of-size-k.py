class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        j=0
        r=[]
        f=""
        for i in range(len(s)//k):
            r.append(s[j:j+k])
            j+=k
        if s[j:]:
            f=s[j:]+"".join([fill]*(k-len(s[j:])))
            r.append(f)
        return r