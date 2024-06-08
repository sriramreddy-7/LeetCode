class Solution:
    def reverse(self, x: int) -> int: 
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if x>0:
            if str(x)[-1]!=0:
                rx= int(str(x)[::-1])
            if str(x)[-1]==0:
                rx= int(str(x)[::-2])
        else:
            if str(x)[-1]!=0:
                flag=int(str(x).replace("-","")[::-1])
                rx= -flag
            if str(x)[-1]==0:
                flag = int(str(x).replace("-", "")[::-2])
                rx= -flag

        if rx < INT_MIN or rx > INT_MAX:
            return 0
        else:
            return rx