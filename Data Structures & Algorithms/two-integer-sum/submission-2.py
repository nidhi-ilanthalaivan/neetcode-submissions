class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store dictionary of pure compliments
        compliment = {}
        for i in range(len(nums)):
            curr_compliment = target - nums[i]
            if curr_compliment in compliment:
                return [compliment[curr_compliment],i]
            compliment[nums[i]] = i

        # first parse - i is 0 nums[i] = 3
        #curr compliment = 4
        #obvi 4 is not yet stored its not yet parsed 
        #so we would like to store it
        # basically for 3 to reach target it needs 4 
        # so we save in compliment
        # compliment becomes {3:0}
        # next parse - i is 1 so nums[i] = 4
        # curr compliment is 3
        # and 3 actually exists in compliment
        # compliment[curr_compliment ] - compliment[3] = 0
        # soit returns[0, 1]

