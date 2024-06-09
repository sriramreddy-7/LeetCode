class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s=""
        for i in word:
            if i==ch:
                i=word.index(ch)
                s=word[:i+1][::-1]+word[i+1:]
                return s
        else:
            return word