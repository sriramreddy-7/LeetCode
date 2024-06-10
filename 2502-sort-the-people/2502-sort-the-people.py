class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        heights.sort(reverse=True)
        names=[]
        for i in heights:
            for k,v in d.items():
                if i==k:
                    names.append(v)
        return names