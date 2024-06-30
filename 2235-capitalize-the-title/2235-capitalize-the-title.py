class Solution:
    def capitalizeTitle(self, title: str) -> str:
        r=title.split(" ")
        title=""
        for i in range(len(r)):
            if i!=0:
                if len(r[i])>2:
                    title=title+" "+r[i].capitalize()
                else:
                    title=title+" "+r[i].lower()
            else:
                if len(r[i])>2:
                    title=title+r[i].capitalize()
                else:
                    title=title+r[i].lower()
        return title