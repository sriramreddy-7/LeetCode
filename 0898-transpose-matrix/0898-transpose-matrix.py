class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])
        tm=[[0 for i in range(r)] for i in range(c)]
        for i in range(r):
            for j in range(c):
                tm[j][i]=matrix[i][j]
        return tm