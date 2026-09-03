class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxofcurr =0
        l=0
        res=[]
        o=[]
        for r in range(len(nums)):
            o.append(nums[r])
            if r-l+1 ==k:
                res.append(max(o))
                o.remove(nums[l])
                l+=1
                
        return res
