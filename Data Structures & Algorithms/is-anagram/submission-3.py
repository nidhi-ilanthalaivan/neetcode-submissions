class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for i in s:
            if i in sDict:
                sDict[i] += 1
            else:
                sDict[i] = 1
        
        for j in t:
            if j in tDict:
                tDict[j] += 1
            else:
                tDict[j] = 1
        
        return sDict == tDict        