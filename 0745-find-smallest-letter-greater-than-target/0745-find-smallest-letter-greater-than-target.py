class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        r=[]
        for i in letters:
            if ord(i)>ord(target):
                r.append(i)
        if r:
            me=r[0]
            for j in r:
                if ord(j)<ord(me):
                    me=j
            return me
        
        else:
            return letters[0] 