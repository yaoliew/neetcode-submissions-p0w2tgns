class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(0, i):
                prefix[i] *= nums[j]
        
        suffix = [1 for i in range(len(nums))]

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                suffix[i] *= nums[j]
        
        ans = [suffix[i] * prefix[i] for i in range(len(nums))]
        return ans