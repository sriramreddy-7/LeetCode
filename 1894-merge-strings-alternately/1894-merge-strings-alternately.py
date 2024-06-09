class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        i = 0
        n = max(len(word1), len(word2))
        while i < n:
            if i < len(word1):
                s += word1[i]
            if i < len(word2):
                s += word2[i]
            i += 1
        return s