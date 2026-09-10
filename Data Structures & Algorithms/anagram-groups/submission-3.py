class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            keys = tuple(count)
            if keys not in groups:
                groups[keys] = []
            groups[keys].append(word)
        return list(groups.values())
        