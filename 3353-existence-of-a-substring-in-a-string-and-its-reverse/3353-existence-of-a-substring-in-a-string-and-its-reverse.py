class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        def reverse(s,x):
            if x in s[::-1]:
                print(x)
                return True
            else:
                return False

        def check(s):
            for i in range(len(s)-1):
                if reverse(s,s[i]+s[i+1]):
                    return True
                else:
                    continue
            else:
                return False

        return check(s)