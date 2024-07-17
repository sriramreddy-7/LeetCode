class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.split()
        r=""
        for i in range(len(t)):
            if i!=len(t)-1:
                r=r+t[i][::-1]+" "
            else:
                r=r+t[i][::-1]
        return r