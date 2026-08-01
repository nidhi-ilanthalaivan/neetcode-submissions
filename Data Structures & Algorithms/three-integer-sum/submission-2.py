class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        best_arrays = []
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1 
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    best_arrays.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
        return best_arrays