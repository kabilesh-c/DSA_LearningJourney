class Solution:

    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)

        total_len = word_len * word_count

        need = {}

        for word in words:
            need[word] = need.get(word, 0) + 1

        result = []

        for i in range(len(s) - total_len + 1):

            seen = {}

            for j in range(word_count):

                start = i + j * word_len

                word = s[start:start + word_len]

                seen[word] = seen.get(word, 0) + 1

            if seen == need:
                result.append(i)

        return result


obj = Solution()

print(
    obj.findSubstring(
        "barfoothefoobarman",
        ["foo", "bar"]
    )
)