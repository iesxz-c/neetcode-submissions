class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left =[1]*n
        right=[1]*n
        l=1
        r=1
        for i in range(n):
            j=-i-1
            left[i] = l
            right[j] = r
            l*=nums[i]
            r*=nums[j]
        return [l*r for l,r in zip(left,right)]