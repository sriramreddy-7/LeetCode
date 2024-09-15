class Solution:
    def countSegments(self, s: str) -> int:
        # sc="!@#$%^&*()_+=,.:"
        # si=" "
        # res=[]
        # temp=""
        # for i in s:
        #     if i not in sc and i not in si:
        #         temp+=i
        #     else:
        #         if temp!="":
        #             res.append(temp)
        #             temp=""
        # if temp!="":
        #     res.append(temp)
        # return len(res)
        se=s.split()
        return len(se)