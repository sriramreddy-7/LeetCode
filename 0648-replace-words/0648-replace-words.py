class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def partition(dictionary,s):
            for word in dictionary:
                if word==s[:len(word)]:
                    return word
            else:
                return False
        dictionary.sort(key=len)
        l=sentence.split()
        s=[]
        r=""
        for i in range(len(l)):
            r=partition(dictionary,l[i])
            if r:
                s.append(r)
            else:
                s.append(l[i])
        return " ".join(s)