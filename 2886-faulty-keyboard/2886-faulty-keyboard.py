class Solution:
    def finalString(self, s: str) -> str:
        if "i" not in s:
            return s
        else:
            k=0
            r=""
            for i in range(len(s)):
                if s[i]=="i":
                    r=r[::-1]+s[i:k][::-1]
                    k=k+1
                else:
                    r=r+s[i]
            return r