class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        final=[]
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                r=[]
                r.append(i)
                d[groupSizes[i]]=r
            else:
                e=d[groupSizes[i]]
                e.append(i)
                d[groupSizes[i]]=e
            if len(d[groupSizes[i]])>=groupSizes[i]:
                final.append(d[groupSizes[i]])
                d[groupSizes[i]]=[]
        return final  