class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
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
# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         l=0
#         r=k-1
#         res=float('inf')
#         while r<len(nums):
#             res=min(res,nums[r]-nums[l])
#             l+=1
#             r+=1
#         return res