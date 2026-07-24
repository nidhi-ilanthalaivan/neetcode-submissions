class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # first step document t into t_dict
        t_dict = {}
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1
        # define need
        need = len(t_dict)
        #define have 
        have = 0
        # define left
        left = 0
        # define best_left
        best_left = 0
        # define best_length
        best_length = float('inf')
        # define sliding window dict
        window_dict = {}
        # for loop
        for right in range(len(s)):
            # documenting current window in window_dict
            window_dict[s[right]] = window_dict.get(s[right], 0) + 1
            # has to match both condiitons like whether this is in t_dict and if the quantity matches the needed quantity in t_dict, then have is incremented
            if s[right] in t_dict and window_dict[s[right]] == t_dict[s[right]]:
                have += 1
            # when have == need, this is a valid substring so we will first document the deets for it
            while have == need:
                if (right - left + 1) < best_length:
                    # essentially documenting smallest indices so far
                    best_length = right - left + 1
                    best_left = left
                if s[left] in t_dict:
                    if window_dict[s[left]] == t_dict[s[left]]:
                        have -= 1
                    window_dict[s[left]] -= 1
                left += 1
            
        if best_length == float('inf'):
            return ""
        else:
            return s[best_left: best_left + best_length]

