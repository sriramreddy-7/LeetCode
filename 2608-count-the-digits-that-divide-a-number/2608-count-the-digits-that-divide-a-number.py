class Solution:
    def countDigits(self, num: int) -> int:
        l=list(map(str,str(num)))
        c=0
        for i in l:
            if num%int(i)==0:
                c=c+1
        return c
