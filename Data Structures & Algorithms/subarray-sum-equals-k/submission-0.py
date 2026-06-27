class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps=[]
        curr = 0
        for i in nums:
            curr+=i
            ps.append(curr)
        c=0
        for i in ps:
            if ps - k == 0 or ps-k == k:
                c+=1
        return c