class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d={}
        def find(i):
            if i.islower() and i.upper() in word:
                if i.lower() not in d:
                    d[i.lower()]=i.upper()
            elif i.isupper() and i.lower() in word:
                if i.lower() not in d:
                    d[i.lower()]=i.upper()
        for i in word:
            find(i)
        return len(d)