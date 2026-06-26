class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==0 or n==1:
            return nums

        m=n//2
        L=nums[:m]
        R=nums[m:]
        L=self.sortArray(L)
        R=self.sortArray(R)

        l,r=0,0

        L_len=len(L)
        R_len=len(R)

        merge=[0]*n
        i=0
        while l<L_len and r< R_len:
            if L[l] < R[r]:
                merge[i] =L[l]
                l+=1
            else:
                merge[i] =R[r]
                r+=1
            i+=1
        while l<L_len:
            merge[i]=L[l]
            l+=1
            i+=1
        while r<R_len:
            merge[i] = R[r]
            r+=1
            i+=1
        return merge
            


# def sortArray(nums):
#     if len(nums) <= 1:
#         return nums

#     mid = len(nums) // 2
#     left = sortArray(nums[:mid])
#     right = sortArray(nums[mid:])

#     return merge(left, right)


# def merge(left, right):
#     i = j = 0
#     merged = []

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1

#     # add remaining elements
#     while i < len(left):
#         merged.append(left[i])
#         i += 1

#     while j < len(right):
#         merged.append(right[j])
#         j += 1

#     return merged