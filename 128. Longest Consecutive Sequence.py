class Solution:

    def longestConsecutive(self, nums):

        numSet = set(nums)

        longest = 0

        for num in numSet:

            if num - 1 not in numSet:

                current = num
                length = 1

                while current + 1 in numSet:

                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


obj = Solution()

print(obj.longestConsecutive([100,4,200,1,3,2]))
print(obj.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))