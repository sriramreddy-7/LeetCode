class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l=list(map(str,sentence.split(" ")))
        for i in range(len(l)):
            if len(l[i])>=len(searchWord):
                if searchWord==l[i][:len(searchWord)]:
                    return i+1
        else:
            return -1