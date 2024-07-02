class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(s,pattern):
            if len(s)!=len(pattern):
                return False
            else:
                d={}
                for i in range(len(s)):
                    if pattern[i] not in d and s[i] not in d.values():
                        d[pattern[i]]=s[i]
                    elif pattern[i] not in d and s[i] in d.values():
                        return False
                    elif d[pattern[i]]!=s[i]:
                        return False
                else:
                    return True
        f=[]
        for i in range(len(words)):
            if check(words[i],pattern):
                f.append(words[i])
        return f