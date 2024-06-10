class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=int(0.05*len(arr))
        nr=arr[n:len(arr)-n]
        mean=sum(nr)/len(nr)
        return round(mean,5)