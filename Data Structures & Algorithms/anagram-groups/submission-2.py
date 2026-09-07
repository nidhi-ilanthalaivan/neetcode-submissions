class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dicts
        group = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            keys = tuple(count)
            if keys not in group:
                group[keys] = []
            group[keys].append(word)
        
        return list(group.values())
        