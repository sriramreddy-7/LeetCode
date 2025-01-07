class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s=set()
        for i in words:
            for j in words:
                if i!=j:
                    if j in i:
                        s.add(j)
        return list(s)
