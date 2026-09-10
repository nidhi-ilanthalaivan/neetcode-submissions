class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for q, j in count.items():
            freq[j].append(q)
        
        result = []
        
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
