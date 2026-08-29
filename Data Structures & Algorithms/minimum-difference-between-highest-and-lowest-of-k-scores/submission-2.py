class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        w=[]
        l=0
        for r in range(len(nums)):
            w.append(nums[r])

            if r-l+1==k:
                ans =min(ans,max(w)-min(w))
                w.remove(nums[l])
                l+=1
        return ans