class Solution:
    def addDigits(self, num: int) -> int:
        def divide(num):
            s=0
            r=0
            while(num>0):
                r=num%10
                s=s+r
                num=num//10
            if s>9:
                return divide(s)
            if s<=9:
                return s
        r=divide(num)
        return r
