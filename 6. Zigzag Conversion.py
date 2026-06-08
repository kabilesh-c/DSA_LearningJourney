class Solution:

    def reverseWords(self, s):

        result = []

        i = len(s) - 1

        while i >= 0:

            # Skip spaces
            while i >= 0 and s[i] == ' ':
                i -= 1

            if i < 0:
                break

            # Mark end of word
            j = i

            # Move to beginning of word
            while i >= 0 and s[i] != ' ':
                i -= 1

            # Extract word
            result.append(s[i + 1:j + 1])

        return " ".join(result)


obj = Solution()

print(obj.reverseWords("the sky is blue"))
print(obj.reverseWords("  hello world  "))
print(obj.reverseWords("a good   example"))