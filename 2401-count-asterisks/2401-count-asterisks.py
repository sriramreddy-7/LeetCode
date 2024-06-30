class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        open=False
        stack=[]
        for i in range(len(s)):
            if s[i]=='|':
                if stack:
                    stack.pop()
                    open=False
                else:
                    stack.append(s[i])
                    open=True
            if open==False and s[i]=="*":
                count+=1
        return count