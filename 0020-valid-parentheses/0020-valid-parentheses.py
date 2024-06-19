class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ob=["{","[","("]
        cb=["}","]",")"]
        for i in range(len(s)):
                if s[i] in ob:
                    stack.insert(0,s[i])
                elif s[i] in cb and stack==[]:
                    return False
                elif s[i] in cb and cb.index(s[i])==ob.index(stack[0]):
                    stack.pop(0)
                else:
                    if s[i] in cb and cb.index(s[i])!=ob.index(stack[0]):
                        return False
        if stack==[]:
            return True
        return False