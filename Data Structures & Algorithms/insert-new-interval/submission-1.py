class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)
        m=[]
        for interval in intervals:
            if not m or m[-1][1]<interval[0]:
                m.append(interval) 
            else:
                m[-1] = [m[-1][0],max(m[-1][1],interval[1])]
        return m
