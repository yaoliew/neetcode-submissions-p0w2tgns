class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x_index, x_value in enumerate(nums[:len(nums) - 1]):
            for y_index, y_value in enumerate(nums[x_index+1:]): 
                if (x_value + y_value == target):
                    return [x_index, y_index + x_index + 1]
