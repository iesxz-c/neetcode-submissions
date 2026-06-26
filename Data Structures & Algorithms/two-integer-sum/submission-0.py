class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        a={}
        for i,j in enumerate(nums):
            k=target-j
            if k not in a:
                a[j] = i
            else:
                return [a[k],i]
        return -1
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return -1