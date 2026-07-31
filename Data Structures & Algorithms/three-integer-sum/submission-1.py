class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        best_array = []
        nums.sort()
        # defining array to store everything valid in
        for i in range(len(nums)):
            # this ensures we skip any duplicate consecutive nums to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # now define left right and target so we dont waste lines of code
            left = i + 1 
            right = len(nums) - 1
            target = -nums[i]
            # now do while left < right to ensure no index out of bounds
            while left < right:
                # general 2 sum logic tbh
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] == target:
                    best_array.append([nums[i], nums[left], nums[right]])
                    # to ensure the left value after it isnt duplicate and wont cause duplicate triplet aka invalid triplet
                    # the purpose of both these while statements is that it will ensure left and right are on their last indice of that duplicate value so when we increment/decrement outside of it, it wont count as an invalid triplet 
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return best_array
