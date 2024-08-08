class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        result=[0]*(k+1) 
        d={}
        for i in logs:
            if i[0] not in d:
                e=set()
                e.add(i[1])
                d[i[0]]=e 
            else:
                s=d[i[0]]
                s.add(i[1])
                d[i[0]]=s
        for k,v in d.items():
            result[len(v)]+=1
        return result[1:]