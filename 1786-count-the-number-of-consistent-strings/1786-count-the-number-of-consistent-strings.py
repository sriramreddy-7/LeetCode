class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        def find(allowed,i):
            for j in i:
                if j not in allowed:
                    return False
            else:
                return True

        for i in words:
            if find(allowed,i):
                count+=1
        return count