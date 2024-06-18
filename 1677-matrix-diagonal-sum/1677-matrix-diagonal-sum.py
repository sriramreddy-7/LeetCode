class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        n=len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i==j or j==n-1:
                    s=s+mat[i][j]
            n=n-1
        return s