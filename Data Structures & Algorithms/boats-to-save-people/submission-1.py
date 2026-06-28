class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        result = 0

        while l <= r:
            remain = limit - nums[r]
            r -= 1
            result += 1

            if l <= r and remain >= nums[l]:
                l += 1

        return result