class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l=text.split(" ")
        bl=[_ for _ in brokenLetters]
        count=0
        fc=0
        for i in l:
            count=0
            for j in bl:
                if j in i:
                    count+=1
            if count>0:
                fc+=1
        return len(l)-fc