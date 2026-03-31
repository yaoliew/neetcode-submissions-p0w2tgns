class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        if len(nums) == 0:
            return 0
        
        seq_length = 1
        for num in set_nums:
            if num - 1 in set_nums:
                continue
            temp = 1
            end_found = False
            while end_found == False:
                if num + temp in set_nums:
                    temp += 1
                else:
                    end_found = True
            seq_length = max(seq_length, temp)
        return seq_length

