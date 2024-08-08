class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=set()
        lose=set()
        d={}
        for i in matches:
            win.add(i[0])
            lose.add(i[1])
            if i[1] not in d:
                d[i[1]]=1 
            else:
                d[i[1]]+=1
        l=[]
        for k,v in d.items():
            if v==1:
                l.append(k)
        l.sort()
        d=[]
        d=list(win-lose)
        d.sort()
        return [d,l]