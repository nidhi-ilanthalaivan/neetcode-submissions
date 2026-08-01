class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # define
        left = 0
        curr_set = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in curr_set:
                    curr_set.remove(s[left])
                    left += 1
            
            curr_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length


