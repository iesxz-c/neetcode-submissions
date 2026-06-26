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
        