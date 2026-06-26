class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = set()
        for r in range(len(nums)):
            if nums[r] in w:
                return True
            w.add(nums[r])

            if len(w)>k:
                w.remove(nums[r-k])
        return False