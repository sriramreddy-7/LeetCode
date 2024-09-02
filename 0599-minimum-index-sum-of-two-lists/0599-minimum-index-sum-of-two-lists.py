class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        for i in range(len(list1)):
            if list1[i] not in d and list1[i]!=" ":
                d[list1[i]]=i
        res={}
        m=set()
        for j in range(len(list2)):
            if list2[j] in d:
                index=j+d[list2[j]]
                if index not in res:
                    e=[]
                    e.append(list2[j])
                    res[index]=e
                    m.add(index)
                else:
                    r=res[index]
                    r.append(list2[j])
                    res[index]=r
        return res[min(m)]

