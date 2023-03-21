def isAnagram(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        list1[:0] = s
        list2[:0] = t
        list2.sort()
        list1.sort()
        if len(list1) == len(list2):
            for a in range(len(list1)):
                if list1[a] != list2[a]:
                    return False
            return True
