class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            else:
                return f(n-1)+f(n-2)
        return f(n)