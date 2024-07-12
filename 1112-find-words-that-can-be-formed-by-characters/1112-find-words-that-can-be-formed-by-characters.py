class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        r=[]
        def check(i):
            f=0
            for j in i:
                if j in chars and i.count(j)<=chars.count(j):
                    pass
                else:
                    return False
            return True

        for i in words:
            if check(i):
                r.append(i)

        return len("".join(r))
