class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use bucket sort - using a dict of size len(num), 
        # make every key a frequency in range len(num),
        # and make every value a list of the array

        count = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for n, f in count.items():
            frequencies[f].append(n)
        
        ans = []
        for i in range(len(frequencies) - 1, 0, -1):
            for x in frequencies[i]:
                ans.append(x)
                if (len(ans) >= k):
                     return ans
