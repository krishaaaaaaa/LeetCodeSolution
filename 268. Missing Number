def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for a in range(len(nums)):
            if len(nums)-a not in nums:
                return len(nums)-a
            elif nums[0] != 0:
                return 0
        return -1
