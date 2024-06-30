class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n=str(num)
        c=0
        for i in range(len(n)):
            if len(n[i:i+k])==k and int(n[i:i+k])!=0 and num%int(n[i:i+k])==0:
                c=c+1
        return c