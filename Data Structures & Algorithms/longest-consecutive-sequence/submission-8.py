class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = cur = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue
            if nums[i] - nums[i-1] == 1:
                cur += 1
            else:
                cur = 1 
            res = max(res, cur)
        return res
