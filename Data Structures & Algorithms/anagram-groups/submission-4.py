class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            key = tuple(count)

            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        return list(groups.values())


        