class Solution:

    def minWindow(self, s, t):

        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        have = 0
        need_count = len(need)

        left = 0

        result_length = float('inf')
        result = [-1, -1]

        for right in range(len(s)):

            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:

                if right - left + 1 < result_length:

                    result_length = right - left + 1

                    result = [left, right]

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        l, r = result

        if result_length == float('inf'):
            return ""

        return s[l:r + 1]


obj = Solution()

print(obj.minWindow("ADOBECODEBANC", "ABC"))