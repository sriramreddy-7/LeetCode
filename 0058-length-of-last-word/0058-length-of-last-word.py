class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = list(s.split(" "))
        d={}
        for i in l:
            if i not in d:
                d[i]=len(i)
        c=0
        for k,v in d.items():
            if k!="":
                c=v
        return c