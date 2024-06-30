class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        d={}
        for i in range(len(releaseTimes)):
            if i==0:
                d[keysPressed[i]]=releaseTimes[i]
            else:
                r=releaseTimes[i]-releaseTimes[i-1]
                if keysPressed[i] not in d:
                    d[keysPressed[i]]=r
                else:
                    if d[keysPressed[i]]<r:
                        d[keysPressed[i]]=r

        mx=0
        s=""
        for k,v in d.items():
            if v>mx:
                mx=v
                if s!="":
                    s=s.replace(s[0],k)
                else:
                    s=k
            if mx==v:
                mx=v
                if ord(k)>ord(s):
                    s=s.replace(s[0],k)
        return s