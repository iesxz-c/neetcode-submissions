class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        w=[]
        mi = float('inf')

        for r in range(len(nums)):
            w.append(nums[r])
            if r-l+1 == k:
                mi = min(mi,max(w) - min(w))
                w.remove(nums[l])
                l+=1
        return mi