class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build hash map to store differences
        seen = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in seen:
                return [seen[difference], i]

            seen[num] = i
            
        