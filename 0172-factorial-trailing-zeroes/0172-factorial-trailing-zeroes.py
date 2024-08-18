class Solution:
    def trailingZeroes(self, n: int) -> int:
        f=1
        for i in range(1,n+1):
            f=f*i
        count = 0
        while f % 10 == 0:
            count += 1
            f = f // 10
        return count