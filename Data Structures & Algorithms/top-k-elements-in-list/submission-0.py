class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i  in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        d=[]
        for i,j in a.items():
            d.append([j,i])
        #print(d)
        d.sort(reverse=True)
        #print(d)

        c=[]
        for i in d:
             c.append(i[1])
        
        return c[:k]

