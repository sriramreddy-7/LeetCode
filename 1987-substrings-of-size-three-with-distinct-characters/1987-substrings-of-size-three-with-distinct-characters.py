class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            if len(s[i:i+3])==3:
                r=set()
                r=set(_ for _ in s[i:i+3])
                if len(r)==3:
                    count+=1
        return count