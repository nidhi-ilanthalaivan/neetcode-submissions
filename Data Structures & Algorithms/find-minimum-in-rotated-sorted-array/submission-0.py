class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # just defining starting left and right
        while left < right:
            mid = (left + right) // 2
            # we didn't do <= bc theres no condition in this problem where there's a proper break yk what i mean n leaving it as <= could cause infinity loop
            # if middle num is greater than last num, by reassigning left to one after mid we know for a fact min has to be in the range from 1 after mid to right as mid is greater than right 
            # example [78912] obvi mid is 2 and 9 > 2 so doing this will ensure left is now 3 aka 1 
            # by running this, obvi you will trigger nums[mid] <= nums[right], so by assigning right to mid, right then equals mid so the while loop stops running after that reassignment and then u j return nums[left] or even nums[right] they should equal the same anyways with the min value
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid 
        return nums[left]
        
