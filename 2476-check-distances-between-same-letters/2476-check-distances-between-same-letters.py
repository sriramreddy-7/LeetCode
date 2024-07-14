class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic={}
        for i in range(len(distance)):
            dic[chr(i+97)]=distance[i]
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                result=i-d[s[i]]
                op=dic.get(s[i])
                if result-1!=op:
                    return False
        else:
            return True