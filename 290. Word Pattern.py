class Solution:

    def wordPattern(self, pattern, s):

        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):

            ch = pattern[i]
            word = words[i]

            if ch in char_to_word:

                if char_to_word[ch] != word:
                    return False

            else:
                char_to_word[ch] = word

            if word in word_to_char:

                if word_to_char[word] != ch:
                    return False

            else:
                word_to_char[word] = ch

        return True


obj = Solution()

print(obj.wordPattern("abba", "dog cat cat dog"))
print(obj.wordPattern("abba", "dog cat cat fish"))
print(obj.wordPattern("abba", "dog dog dog dog"))