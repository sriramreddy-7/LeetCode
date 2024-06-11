class Solution:
    def getLucky(self, s: str, k: int) -> int:
        j=1
        d={}
        for i in range(97,123):
            d[chr(i)]=j
            j=j+1
        ns=""
        for i in s:
            ns=ns+str(d.get(i))
        ns=int(ns)
        s=0
        while k!=0:
            rem=0
            s=0
            while ns>0:
                rem=ns%10
                s=s+rem
                ns=ns//10
            ns=s
            k=k-1
        return ns
