class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_num(i):
            r=str(i)
            _sum=0
            for j in r:
                _sum+=int(j)
            return _sum

        def check(n):
            if n<=9:
                return n
            else:
                d={}
                for i in range(1,n+1):
                    result=sum_num(i)
                    if result not in d:
                        d[result]=1
                    else:
                        d[result]+=1
                size=0
                c=0
                for k,v in d.items():
                    if v>size:
                        size=v
                        c=0
                        c=c+1
                    elif v==size:
                        c=c+1
                return c
        return check(n)