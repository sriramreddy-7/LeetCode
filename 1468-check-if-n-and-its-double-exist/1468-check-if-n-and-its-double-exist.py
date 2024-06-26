class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        def find(m,arr,i):
            for j in range(len(arr)):
                if j!=i and arr[j]==m:
                    return True
            else:
                return False
        for i in range(len(arr)):
            if find(2*arr[i],arr,i):
                return True
        else:
            return False