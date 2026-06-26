from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i,j in Counter(nums).items():
            if (j > len(nums)/2) :
                return i
            else: continue