class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={0:1}
        counts=0
        summ =0
        for i in nums:
            summ += i
            if summ not in a:
                a[summ]=1
            else:
                a[summ]+=1
            counts += a.get(summ-k,0)
        return counts


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
