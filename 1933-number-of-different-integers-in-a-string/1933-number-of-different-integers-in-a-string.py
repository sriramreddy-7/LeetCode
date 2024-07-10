class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        rs=""
        num_array=[]
        for i in word:
            if i.isnumeric():
                rs=rs+i
            else:
                if rs.isnumeric():
                    num_array.append(int(rs))
                    rs=""
        if rs!="":
            num_array.append(int(rs))
        return len(set(num_array))