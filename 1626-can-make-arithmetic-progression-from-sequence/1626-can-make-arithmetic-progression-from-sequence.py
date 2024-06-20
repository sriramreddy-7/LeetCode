class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort(reverse=True)
        cs=0
        for i in range(len(arr)-1):
            if i==0:
                cs=abs(arr[i]-arr[i+1])
            else:
                if cs!=abs(arr[i]-arr[i+1]):
                    return False
        else:
            return True