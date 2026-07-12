class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ok for anagrams hash map is the move bc u can j do 
        # continued - a quick return if blach blah == blach blah to
        # continued - see if they r truly anagrams 
        # however, the doubt is in the mega arr type output code is esxpecting
        # lets try brute force first - like parsing thry each str in strings
        # and creating a hash map for them all and comparing ?
        # ugh idk wait first maybe group with length of strings?
        # 
        groups = {}

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            

            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())