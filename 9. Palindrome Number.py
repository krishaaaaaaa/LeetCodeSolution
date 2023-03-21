def isPalindrome(self, x: int) -> bool:
        list1 = list(str(x))
        list2 = list1[::-1]
        for a in range(len(list1)):
            if list1[a] != list2[a]:
                return False
        return True
        
