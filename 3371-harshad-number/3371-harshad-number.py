class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        num=0
        for i in str(x):
            num=num+int(i)
        if x%num==0:
            return num
        else:
            return -1