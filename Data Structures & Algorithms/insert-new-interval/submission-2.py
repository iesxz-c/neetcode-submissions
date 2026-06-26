class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        target = newInterval[0]
        l=0
        r=n-1
        while l<=r:
            m=l+(r-l)//2
            if intervals [m][0] < target:
                l=m+1
            else:
                r=m-1

        intervals.insert(l,newInterval)
        m=[]
        for interval in intervals:
            if not m or m[-1][1] < interval[0]:
                m.append(interval)
            else:
                m[-1]=[m[-1][0],max(m[-1][1],interval[1])]
        return m