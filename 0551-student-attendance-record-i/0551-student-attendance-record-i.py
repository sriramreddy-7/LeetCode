class Solution:
    def checkRecord(self, s: str) -> bool:
        A=0
        l=0
        for i in s:
            if i=="A":
                A+=1
            elif i=="L":
                l+=1
            if i!="L":
                l=0
            if A>=2 or l>=3:
                return False
        return True
        