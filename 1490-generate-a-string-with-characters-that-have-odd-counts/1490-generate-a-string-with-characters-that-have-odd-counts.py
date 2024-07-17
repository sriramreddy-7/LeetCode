class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            r1="".join(["a"]*(n-1))
            r2="".join(["b"] * 1)
            return r1+r2
        else:
            r=[]
            return "".join([chr(97)] * n)