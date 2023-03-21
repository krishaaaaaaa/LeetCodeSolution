b = strs[0]

        for a in strs:
            while not (a.startswith(b)):
                b = b[:-1]
        return(b)
