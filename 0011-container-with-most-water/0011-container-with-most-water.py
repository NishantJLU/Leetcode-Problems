class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Width between the two lines
            width = right - left

            # Height of water is the smaller line
            h = min(height[left], height[right])

            # Calculate area
            area = width * h

            # Update maximum area
            if area > max_area:
                max_area = area

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area