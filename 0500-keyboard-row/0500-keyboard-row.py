class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1={'w', 'q', 'o', 'p', 'u', 'y', 'e', 't', 'r', 'i'}
        r2={'j', 'h', 'g', 'f', 'k', 'd', 'a', 's', 'l'}
        r3={'z', 'x', 'm', 'n', 'c', 'b', 'v'}
        s1,s2,s3=[],[],[]
        for i in range(len(words)):
            r=set(words[i].lower())
            if r.issubset(r1):
                s1.append(words[i])
            if r.issubset(r2):
                s2.append(words[i])
            if r.issubset(r3):
                s3.append(words[i])
        s4=[s1+s2+s3]
        return max(s4)