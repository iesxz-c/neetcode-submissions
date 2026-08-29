class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d and i-d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False
        # l=0
        # s=set()
        # for r in range(len(nums)):
        #     if nums[r] in s:
        #         return True
        #     s.add(nums[r])
        #     if r-l+1 > k:
        #         s.remove(nums[l])
        #         l+=1
        # return False