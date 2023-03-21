def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        n = "".join(s)
        a = int(n)
        a += 1
        b = list(map(int, str(a)))
        return b
