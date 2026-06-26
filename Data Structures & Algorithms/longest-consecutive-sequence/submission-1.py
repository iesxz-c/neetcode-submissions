class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest =0
        k = set(nums)
        for n in k:
            if n-1 in k:
                continue
            curr = n
            le =1
            while curr+1 in k:
                curr = curr+1
                le+=1
            longest = max(le, longest)
        return longest