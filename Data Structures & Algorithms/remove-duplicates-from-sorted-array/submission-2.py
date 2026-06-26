class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u=1
        l=1
        while l<len(nums):
            if nums[l] != nums[u-1]:
                nums[u] = nums[l]
                u+=1
                l+=1
            else:
                l+=1
        return u