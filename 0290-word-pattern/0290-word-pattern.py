class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split()
        if len(l)!=len(pattern):
            return False
        d={}
        for i in range(len(pattern)):
            if pattern[i] not in d and l[i] not in d.values():
                d[pattern[i]]=l[i]
            elif pattern[i] not in d and l[i] in d.values():
                return False
            elif d[pattern[i]]!=l[i]:
                return False

        return True