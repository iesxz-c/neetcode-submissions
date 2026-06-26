class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxwa = 0
        l=0
        r=n-1
        while l<r:
            area = min(heights[l],heights[r]) * (r-l)
            maxwa= max(maxwa,area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxwa
        # n = len(heights)
        # maxwa = 0
        
        # for i in range(n):

        #     for j in range(i+1,n):
        #         area = min(heights[i],heights[j]) * (j-i)
        #         maxwa = max(maxwa,area)
        # return maxwa
