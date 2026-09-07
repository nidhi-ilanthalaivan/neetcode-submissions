class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in storage:
                return [storage[compliment], i]
            storage[nums[i]] = i
        