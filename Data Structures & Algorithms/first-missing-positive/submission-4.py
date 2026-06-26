class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        a={}
        for i in range(1,n+1):
            a[i] = False
        
        for i in nums:
            if i in a:
                a[i] = True
        for i in range(1, n + 1):
            if a[i] == False:
                return i
        return n + 1
        
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         x=[]
#         k = set(nums)
#         for i in k :
#             if i>0:
#                 x.append(i)
#         x.sort()
#         ex=1
#         for i in x :
#             if i<ex :
#                 continue
#             elif i == ex:
#                 ex += 1
#             else:
#                 return ex
#         return ex