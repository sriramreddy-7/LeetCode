class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m=len(word1),len(word2)
        emp=""
        if n==m:
            for i in range(n):
                emp+=word1[i]
                emp+=word2[i]
        elif n>m:
            i=0
            while i<m:
                emp += word1[i]
                emp += word2[i]
                i=i+1
            emp+=word1[i:]
        else:
            i=0
            while i<n:
                emp += word1[i]
                emp += word2[i]
                i+=1
            emp+=word2[i:]
        return emp