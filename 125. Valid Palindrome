def isPalindrome(self, s: str) -> bool:
        b = s.replace(" ", "")
        c = b.replace(',','')
        punc = '''!()-[]{};:`'"\,<>./?@#$%^&*_~'''
        for e in c:
            if e in punc:
                c = c.replace(e,'')
        a = list(c.lower())
        z = list(reversed(a))
        if a == z:
            return True
