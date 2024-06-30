class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f1,f2,t="","",""
        for i in firstWord:
            f1=f1+str((ord(i)-97))
        for i in secondWord:
            f2=f2+str((ord(i)-97))
        for i in targetWord:
            t = t + str((ord(i)-97))
        f1=int(f1)
        f2=int(f2)
        t=int(t)
        if f1+f2==t:
            return True
        else:
            return False