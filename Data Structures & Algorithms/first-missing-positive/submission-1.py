class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        x=[]
        for i in nums :
            if i>0:
                x.append(i)
        k = set(x)
        ex=1
        for i in k :
            if i<ex :
                continue
            elif i == ex:
                ex += 1
            else:
                return ex
        return ex