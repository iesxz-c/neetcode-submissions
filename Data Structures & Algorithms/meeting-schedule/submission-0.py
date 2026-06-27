"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        curr=intervals[0].end
        for i in intervals[1:]:
            if i.start > curr:
                curr = i.end
            else:
                return False
        return True

