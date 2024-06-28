class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            j=0
        elif ruleKey == "color":
            j=1
        else:
            j=2
        c=0
        for i in range(len(items)):
            if items[i][j]==ruleValue:
                c=c+1
        return c
