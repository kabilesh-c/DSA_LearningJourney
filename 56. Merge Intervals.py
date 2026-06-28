class Solution:

    def merge(self, intervals):

        intervals.sort()

        merged = [intervals[0]]

        for start, end in intervals[1:]:

            last_end = merged[-1][1]

            if start <= last_end:

                merged[-1][1] = max(
                    last_end,
                    end
                )

            else:

                merged.append([start, end])

        return merged


obj = Solution()

print(
    obj.merge(
        [[1,3],[2,6],[8,10],[15,18]]
    )
)

print(
    obj.merge(
        [[1,4],[4,5]]
    )
)