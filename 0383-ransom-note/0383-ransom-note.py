class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r="".join(set(ransomNote))
        for i in r:
            if i in magazine:
                if magazine.count(i)<ransomNote.count(i):
                    return False
            else:
                return False
        return True