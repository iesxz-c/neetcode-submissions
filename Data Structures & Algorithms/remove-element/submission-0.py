class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        u=0
        for l in range(len(nums)):
            if nums[l] != val :
                nums[u] = nums[l]
                l+=1
                u+=1

            else:
                l+=1
        return u    