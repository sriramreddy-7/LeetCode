class Solution:
    def reformatDate(self, date: str) -> str:
        month ={"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, 
        "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        l=list(date.split(" "))
        d=month.get(l[1])
        r=["th","nd","rd","st"]
        i=l[0][-2]+l[0][-1]
        if  i in r:
            l[0]=l[0].replace(i,"")
        l[0]=int(l[0])
        if d<10 and l[0]<10:
            return f"{l[2]}-{0}{d}-{0}{l[0]}"
        elif d<10:
            return f"{l[2]}-{0}{d}-{l[0]}"
        elif l[0]<10:
            return f"{l[2]}-{d}-{0}{l[0]}"
        else:
            return f"{l[2]}-{d}-{l[0]}"