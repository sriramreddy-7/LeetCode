class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        n=len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+n]==needle:
                return i
        else:
            return -1