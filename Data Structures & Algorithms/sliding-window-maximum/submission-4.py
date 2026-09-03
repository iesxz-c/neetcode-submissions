class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or len(nums) ==1:
            return nums
        maxofcurr =0
        l=0
        res=[]
        for r in range(len(nums)):
            maxofcurr = max(maxofcurr, nums[r])
            if r-l+1 ==k:
                res.append(maxofcurr)
                maxofcurr = max(nums[l:l+k])
                l+=1
                
        return res
