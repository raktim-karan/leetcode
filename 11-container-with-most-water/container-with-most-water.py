class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the width and the limiting height
            width = right - left
            current_height = min(height[left], height[right])
            
            # Update max_water if the current container holds more
            max_water = max(max_water, width * current_height)
            
            # Greedily move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water