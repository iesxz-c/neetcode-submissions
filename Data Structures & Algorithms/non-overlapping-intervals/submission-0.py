class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c=0
        curr=intervals[0][1]
        for interval in intervals[1:] :
            if interval[0] >=  curr :
                curr = interval[1]
            else:
                c+=1
            # curr = interval[1]
        return c