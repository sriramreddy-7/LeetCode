class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        else:
            f=[]
            k=0
            for i in range(m):
                r = []
                for j in range(n):
                    r.append(original[k])
                    k=k+1
                f.append(r)
            return f