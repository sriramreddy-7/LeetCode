class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        l=[]
        def check(x):
            try:
                x=int(x)
                return x
            except:
                if x.isalpha() or x.isalnum():
                    return len(x)
                if x.isnumeric():
                     return int(x)

        for i in strs:
            l.append(check(i))
        return max(l)
