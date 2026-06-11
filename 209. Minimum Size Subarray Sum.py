class Solution:

    def minSubArrayLen(self, target, nums):

        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):

            current_sum += nums[right]

            while current_sum >= target:

                min_length = min(
                    min_length,
                    right - left + 1
                )

                current_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length


obj = Solution()

print(obj.minSubArrayLen(7, [2,3,1,2,4,3]))
print(obj.minSubArrayLen(4, [1,4,4]))
print(obj.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))