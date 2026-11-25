class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        k_list = []
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        new_counts = sorted(counts, key = counts.get, reverse = True)

        for i in range(k):
            k_list.append(new_counts[i])
        return k_list
        