class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n):
            if nums[i]>0:
                break
            elif i>0 and nums[i] == nums[i-1]:
                continue
            lo =i+1
            high = n-1
            while lo<high:
                summ = nums[lo] + nums[high] + nums[i]
                if summ == 0:
                    res.append([nums[i],nums[lo],nums[high]])
                    lo+=1
                    high -=1
                elif summ >0:
                    high -=1
                else:
                    lo+=1
        return res