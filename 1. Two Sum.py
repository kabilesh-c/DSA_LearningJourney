class Solution:

    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i


obj = Solution()

print(obj.twoSum([2,7,11,15], 9))
print(obj.twoSum([3,2,4], 6))
print(obj.twoSum([3,3], 6))