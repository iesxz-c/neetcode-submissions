class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        a={}
        l=0
        ans=0
        total =0
        for r in range(len(fruits)):
            a[fruits[r]] = a.get(fruits[r],0)+1
            if len(a) > 2:
                a[fruits[l]] -=1   
                if a[fruits[l]] == 0:
                    del a[fruits[l]]
                l+=1
            ans = max(ans,r-l+1)
        return ans