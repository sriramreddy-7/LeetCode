class Solution:
    def isFascinating(self, n: int) -> bool:
        st=str(n)+str(n*2)+str(n*3)
        s=set()
        for i in st:
            if i=="0":
                return False
            else:
                s.add(i)
        if len(s)!=len(st):
            return False
        return True