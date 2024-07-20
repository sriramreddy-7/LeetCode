class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        def check(x,p):
            for i in range(len(p)):
                if p[i]<=x:
                    return p[i]
            return False
        answer=[]
        for i in range(len(prices)):
            if prices[i+1:]:
                r=check(prices[i],prices[i+1:])
                if r:
                    answer.append(prices[i]-r)
                else:
                    answer.append(prices[i])
            else:
                answer.append(prices[i])
        return answer