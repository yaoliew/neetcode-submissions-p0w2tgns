class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequencies = dict()

        for num in nums:
            if num in num_frequencies:
                num_frequencies[num] += 1
            else:
                num_frequencies[num] = 1

        sorted_tuples = sorted(num_frequencies.items(), key=lambda x:x[1], reverse=True)
        return [x[0] for x in sorted_tuples[:k]]