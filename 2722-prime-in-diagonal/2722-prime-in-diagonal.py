class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def prime(x):
            if x<2:
                return False
            for i in range(2,int(x ** 0.5) + 1):
                if  x%i==0:
                    return False
            else:
                return True
        _max=0
        n=len(nums)
        for i in range(n):
            if prime(nums[i][i]) and nums[i][i] > _max:
                _max = nums[i][i]
            if prime(nums[i][n - 1 - i]) and nums[i][n - 1 - i] > _max:
                _max = nums[i][n - 1 - i]   
        return _max
