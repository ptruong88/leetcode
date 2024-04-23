# https://leetcode.com/problems/merge-intervals/description/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

 

# Constraints:

#     1 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 104

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort() #self.sort_intervals(intervals)
        # sorted_intervals = intervals
        index = 0
        result = []
        while index < len(intervals):
            current_interval = intervals[index]
            # print("---current_interval {}".format(current_interval))
            # print("---result {}".format(result))
            if len(result) == 0:
                result.append(current_interval)
            else:
                latest_merged_interval = result[len(result)-1]
                if self.is_overlap(current_interval, latest_merged_interval) is True:
                    new_interval = self.merge_intervals(current_interval, latest_merged_interval)
                    result[len(result)-1] = new_interval
                else:
                    result.append(current_interval)
            
            index += 1

        return result
        
    def is_overlap(self, range1, range2):
        return self.is_range_in_range(range1, range2) or self.is_range_in_range(range2, range1)

    def is_range_in_range(self, range1, range2):
        for r in range1:
            if self.is_in_range(r, range2):
                return True
        return False

    def is_in_range(self, num, nums):
        if num >= nums[0] and num <= nums[1]:
            return True
        return False

    def merge_intervals(self, interval1, interval2):
        # print("---interval1 {}".format(interval1))
        # print("---interval2 {}".format(interval2))
        start = interval1[0] if interval1[0] < interval2[0] else interval2[0]
        end = interval1[1] if interval1[1] > interval2[1] else interval2[1]
        return [start,end]

    # def sort_intervals(self, intervals):
    #     start_intervals = []
    #     for i in intervals:
    #         if i[0] not in start_intervals:
    #             start_intervals.append(i[0])
    #     start_intervals.sort()

    #     copied_intervals = intervals.copy()
    #     sorted_intervals = []
    #     for start_interval in start_intervals:
    #         index = 0
    #         while index < len(copied_intervals):
    #             interval = copied_intervals[index]
    #             if interval[0] == start_interval:
    #                 sorted_intervals.append(interval)
    #                 copied_intervals.pop(index)
    #         index += 1
    #     return sorted_intervals
        