class Solution:
    def freqAlphabets(self, s: str) -> str:
        ash=[]
        d={}
        for i in range(1,27):
            if i>=1 and i<=9:
                d[str(i)]=chr(96+i)
            if i>=10 and i<=26:
                d[f"{i}#"]=chr(96+i)
        for i in range(len(s)):
            if s[i]=="#":
                ash.append(i)
        i,j=0,0
        r=""
        while i<len(s):
            if j<len(ash) and i+2==ash[j]:
                r=r+d.get(s[i:i+3])
                j=j+1
                i=i+3
            else:
                r=r+d.get(s[i])
                i=i+1
        return r