class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # define left and right
        left = 0
        right = len(heights) - 1
        # define storage var
        best_area = 0
        while left < right:
            width = right - left
            best_area = max(best_area, width * min(heights[left], heights[right]))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return best_area


        #ideally it would be returning width x min(heights[left], heights[right])
        