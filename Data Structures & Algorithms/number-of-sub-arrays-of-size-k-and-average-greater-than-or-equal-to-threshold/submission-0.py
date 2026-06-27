class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        count =0
        w=0
        for r in range(len(arr)):
            w+=arr[r]
            if r-l+1 ==k:
                if w/k >= threshold:
                    count+=1
                w-=arr[l]
                l+=1
        return count