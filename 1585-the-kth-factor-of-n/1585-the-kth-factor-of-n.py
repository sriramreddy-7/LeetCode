class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        l=[i for i in range(1,n+1) if n%i==0]
        try:
            return l[k-1]
        except:
            return -1