class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # once this while statement stops that means that whatever j is, that indice is directly #
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i += length
        
        return res
            
