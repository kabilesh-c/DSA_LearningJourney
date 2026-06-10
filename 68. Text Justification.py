class Solution:

    def fullJustify(self, words, maxWidth):

        result = []
        i = 0

        while i < len(words):

            line_words = []
            line_length = 0

            while i < len(words) and line_length + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_length += len(words[i])
                i += 1

            spaces = maxWidth - line_length
            gaps = len(line_words) - 1

            if i == len(words) or gaps == 0:

                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))

            else:

                even_spaces = spaces // gaps
                extra_spaces = spaces % gaps

                line = ""

                for j in range(gaps):

                    line += line_words[j]

                    line += " " * even_spaces

                    if j < extra_spaces:
                        line += " "

                line += line_words[-1]

            result.append(line)

        return result


obj = Solution()

words = ["This","is","an","example","of","text","justification."]
maxWidth = 16

for line in obj.fullJustify(words, maxWidth):
    print(f'"{line}"')