class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for i in range(len(words)):
            if words[i]>=pref:
                if pref==words[i][0:len(pref)]:
                    c=c+1
        return c