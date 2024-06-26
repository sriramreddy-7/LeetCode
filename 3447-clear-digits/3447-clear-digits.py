class Solution:
    def clearDigits(self, s: str) -> str:
        if s.isalpha():
            return s
        else:
            r=[]
            for i in range(len(s)):
                if s[i].isalpha():
                    r.append(s[i])
                else:
                    if r:
                        r.pop()
            if r:
                return "".join(r)
            return ""