class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        r=separator.join(words)
        s=r.split(separator)
        words=[]
        for i in s:
            if i!="":
                words.append(i)
        return words