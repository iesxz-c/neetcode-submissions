class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        l=0
        r=n-1
        res=0
        while l<=r:
            if people[l] + people[r] <= limit:
                l+=1
                r-=1
                res+=1
            elif people[l] == limit:
                res+=1
                l+=1
            else:
                res+=1
                r-=1
            

        
        return res
