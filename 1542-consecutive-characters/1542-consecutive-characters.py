class Solution:
    def maxPower(self, s: str) -> int:
        r=1
        d=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                r=r+1
            else:
                if d and r>d[-1]:
                    d.append(r)
                else:
                    d.append(r)
                r=1
        d.append(r)
        if d:
            return max(d)
        return 1