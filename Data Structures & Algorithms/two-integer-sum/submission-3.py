class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_store = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in compliment_store:
                return [compliment_store[compliment], i]
            compliment_store[nums[i]] = i 
        
        