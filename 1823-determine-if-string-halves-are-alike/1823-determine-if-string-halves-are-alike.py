class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s1=s[:len(s)//2]
        s2=s[len(s)//2:]
        if s1==s2:
            return False
        else:
            c=0
            k=0
            for i in s1:
                if i in vowels:
                    c=c+1
            for j in s2:
                if j in vowels:
                    k=k+1
            if c==k:
                return True
            else:
                return False