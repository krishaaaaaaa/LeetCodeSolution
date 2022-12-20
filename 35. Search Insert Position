def searchInsert(self, nums: List[int], target: int) -> int:
        if nums.count(target) == 1:
            return (nums.index(target))
        elif target > nums[len(nums) - 1]:
            return (len(nums))
        else:
            for a in nums:
                if target < a:
                    return (nums.index(a))
        
