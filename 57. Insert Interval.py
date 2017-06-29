# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # I am strongly astonished by this incredible code, by StefanPochmann.
        s, e = newInterval.start, newInterval.end
        parts = merge, left, right = [], [], []
        for i in intervals:
            parts[(i.end<s)-(i.start>e)].append(i)
        s,e = [min(s,merge[0].start),max(e,merge[-1].end)] if merge else [s,e]
        return left + [Interval(s,e)] + right
