class Solution:
    def thousandSeparator(self, n: int) -> str:
        n=str(n)
        s=""
        c=0
        for i in range(len(n)-1,-1,-1):
            s=s+n[i]
            c=c+1
            if c==3 and i!=0:
                s=s+"."
                c=0
        return s[::-1]