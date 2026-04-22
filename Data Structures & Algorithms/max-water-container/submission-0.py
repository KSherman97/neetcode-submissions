class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the best solution is probably a sliding windows type solution
        left = 0
        right = len(heights)-1

        max_volume = 0

        print(f"{left} {right}")

        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            
            if volume > max_volume:
                max_volume = volume

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_volume
