class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0

        r=len(arr)-1
        while r-l+1 > k:
            left = abs(x-arr[l])
            right = abs(x - arr[r])
            if left > right :
                l+=1
            elif left == right:
                r-=1
            else:

                r-=1
        return arr[l:r+1]

