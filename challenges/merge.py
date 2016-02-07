__author__ = 'cloudera'


def merge(intervals):
        if len(intervals) == 1:
            return intervals
        # sort
        for i in xrange(1, len(intervals)):
            key = intervals[i]
            j = i-1
            while j>=0 and key[0]<intervals[j][0]:
                intervals[j+1] = intervals[j]
                j -= 1
            intervals[j+1] = key

        k = 0
        l = 1
        while l<len(intervals):
            if max(intervals[k][0], intervals[l][0])<=min(intervals[k][1], intervals[l][1]):
                merged_item = [min(intervals[k][0], intervals[l][0]), max(intervals[k][1], intervals[l][1])]
                intervals[k] = merged_item
                del intervals[l]
            else:
                k += 1
                l += 1
        return intervals


print merge([[1,10],[2,9],[3,8],[4,7],[5,6],[6,6]])