class Solution:

    def canConstruct(self, ransomNote, magazine):

        count = {}

        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        for ch in ransomNote:

            if ch not in count or count[ch] == 0:
                return False

            count[ch] -= 1

        return True


obj = Solution()

print(obj.canConstruct("a", "b"))
print(obj.canConstruct("aa", "ab"))
print(obj.canConstruct("aa", "aab"))