class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in range(len(items1)):
            if items1[i][0] not in d:
                d[items1[i][0]]=items1[i][1]
        for i in range(len(items2)):
            if items2[i][0] not in d:
                d[items2[i][0]]=items2[i][1]
            else:
                d[items2[i][0]]+=items2[i][1]
        dic=dict(sorted(d.items()))
        result=[]
        for k,v in dic.items():
            result.append([k,v])
        return result