class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=[]
        k = set(nums)
        for i in k :
            if i>0:
                x.append(i)
        x.sort()
        ex=1
        for i in x :
            if i<ex :
                continue
            elif i == ex:
                ex += 1
            else:
                return ex
        return ex