class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={0:1}
        curr=0
        c=0
        for i in nums:
            curr += i
            if curr - k in a:
                c+=a[curr-k]
            a[curr] = a.get(curr, 0) + 1
        return c


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         c=0
#         for i in range(len(nums)):
#             su = nums[i]
#             if su == k:
#                 c += 1
#             for j in range(i+1,len(nums)):
#                 su += nums[j]
#                 if su == k:
#                     c+=1
#         return c
