class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text)<5:
            return 0
        b="balon"
        d={}
        for i in text:
            if i in b:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        def check():
            if len(d)<5:
                return 0
            c = set()
            for k,v in d.items():
                flag=0
                if k=="o" or k=="l":
                    if v>=2:
                        if v%2==0:
                            c.add(v//2)
                        else:
                            c.add((v-1)//2)
                    else:
                        return 0
                else:
                    c.add(v)
            return min(c)
        return check()