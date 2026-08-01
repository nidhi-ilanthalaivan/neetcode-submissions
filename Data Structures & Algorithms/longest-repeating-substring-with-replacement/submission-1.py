class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #obvi define left, curr_dict, max_freq
        left = 0
        curr_dict = {}
        max_freq = 0
        best_length = 0
        for right in range(len(s)):
            curr_dict[s[right]] = curr_dict.get(s[right], 0) + 1
            max_freq = max(max_freq, curr_dict[s[right]])
            while (right - left + 1) - max_freq > k:
                curr_dict[s[left]] -= 1
                left += 1
            best_length = max(best_length, right - left + 1)
        return best_length