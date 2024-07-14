class Solution:
    def replaceDigits(self, s: str) -> str:
        r=""
        for i in range(len(s)):
            if i%2!=0:
                r=r+chr(ord(s[i-1])+int(s[i]))
            else:
                r=r+s[i]
        return r