def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/ 2
        num = set(nums)
        for a in num:
            b = nums.count(a)
            if b > n:
                return a
