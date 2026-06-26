from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        c = Counter(nums)
        po=0
        for i in [0,1,2]:
            for _ in range(c[i]):
                nums[po] = i
                po+=1
            