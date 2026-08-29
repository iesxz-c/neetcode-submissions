class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        running = 0
        l=0
        c=0
        for r in range(len(arr)):
            running += arr[r]
            if r-l+1 == k:
                if running/k >= threshold:
                    c+=1
                running -= arr[l]
                l+=1
        return c