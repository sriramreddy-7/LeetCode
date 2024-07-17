class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        r=[]
        def check(x,start,end):
            t=[]
            for k in range(start,end+1):
                t.append(f"{chr(x)}{k}")
            return t
        for i in range(ord(s[0]),ord(s[-2])+1):
            r.extend(check(i,int(s[1]),int(s[-1])))
        return r