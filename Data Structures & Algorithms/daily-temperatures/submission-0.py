class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [0] * n
        stack = []

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                old_day = stack.pop()
                result[old_day] = i - old_day
            stack.append(i)
        
        return result