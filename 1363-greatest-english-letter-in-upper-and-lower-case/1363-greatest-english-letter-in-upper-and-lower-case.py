class Solution:
    def greatestLetter(self, s: str) -> str:
        f=set()
        for j in s:
            if j.islower():
                if j.upper() in s:
                    f.add(j)
            else:
                if j.lower() in s and j.upper() not in f:
                    f.add(j)

        if f:
            return max(f).upper()
        else:
            return ""