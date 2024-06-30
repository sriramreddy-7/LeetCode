class Solution:
    def secondHighest(self, s: str) -> int:
        n=set()
        for i in s:
            if i.isnumeric():
                n.add(int(i))
        n=list(n)
        n.sort()
        if len(n)>1:
            return n[-2]
        else:
            return -1