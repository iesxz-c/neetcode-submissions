from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        pos=0
        c= Counter(nums)
        for i in [0,1,2]:
           for _ in range(c[i]):
               nums[pos] = i
               pos+=1
                    