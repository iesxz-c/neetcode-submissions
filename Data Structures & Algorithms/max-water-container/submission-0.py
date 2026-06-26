class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxwa = 0
        
        for i in range(n):

            for j in range(i+1,n):
                area = min(heights[i],heights[j]) * (j-i)
                maxwa = max(maxwa,area)
        return maxwa
