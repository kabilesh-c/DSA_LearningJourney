class Solution:

    def lengthOfLastWord(self, s):

        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0

        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


obj = Solution()

print(obj.lengthOfLastWord("Hello World"))
print(obj.lengthOfLastWord("   fly me   to   the moon  "))
print(obj.lengthOfLastWord("luffy is still joyboy"))