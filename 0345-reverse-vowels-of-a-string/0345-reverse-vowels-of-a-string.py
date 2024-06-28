class Solution:
    def reverseVowels(self, s: str) -> str:
        r=[_ for _ in s]
        i=0
        j=len(s)-1
        s=""
        v=["a","e","i","o","u","A","E","I","O","U"]
        while i<=j:
            if r[i] in v and r[j] in v:
                r[i],r[j]=r[j],r[i]
                i=i+1
                j=j-1
            elif r[i] not in v and r[j] not in v:
                i=i+1
                j=j-1
            elif r[i] not in v:
                i=i+1
            elif r[j] not in v:
                j=j-1
        return "".join(r)