class Solution:
    def digitCount(self, num: str) -> bool:
        n=len(num)
        for i in range(n):
            if num.count(str(i))!=int(num[i]):
                return False
        return True