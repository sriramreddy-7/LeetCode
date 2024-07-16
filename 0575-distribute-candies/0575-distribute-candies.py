class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dc=len(set(candyType))
        n=len(candyType)//2
        def  candy(dc,n):
            if n<=dc:
                return n
            elif dc<n:
                return dc
        return candy(dc,n)