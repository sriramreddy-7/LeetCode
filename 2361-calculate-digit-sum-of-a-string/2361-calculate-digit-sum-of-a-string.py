class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s)<=k:
            return s
        def divide(x, k):
            j = 0
            r = []
            for i in range(len(x) // k):
                r.append(x[j:j + k])
                j = j + k
            if x[j:]:
                r.append(x[j:])
            return r
        
        def check(s, k):
            while True:
                r = divide(s, k)
                sum_array = []
                for chunk in r:
                    ss = sum(int(digit) for digit in chunk)
                    sum_array.append(ss)
                s = "".join(map(str, sum_array))
                if len(s) <= k:
                    return s
        
        return check(s, k)
