class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        m=0
        s=0
        c=0
        while n:
            for i in grid:
                c=max(i)
                i.remove(c)
                if c>m:
                    m=c
            s=s+m
            m=0
            n=n-1
        return s