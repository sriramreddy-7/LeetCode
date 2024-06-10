class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        f=[v for k,v in d.items()]
        if len(f)==len(set(f)):
            return True
        return False