class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def email(e):
            email=e.split("@")
            if "." in email[0]:
                email[0]=email[0].replace(".","")
            if "+" in email[0]:
                f=email[0].find("+")
                email[0]=email[0][:f]
            return email[0]+"@"+email[1]
        s=set()
        for i in emails:
            r=email(i)
            s.add(r)
        return len(s)