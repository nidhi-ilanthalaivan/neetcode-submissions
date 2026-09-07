class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sHashMap = {}
        tHashMap = {}

        for i in s:
            if i in sHashMap:
                sHashMap[i] += 1
            else:
                sHashMap[i] = 1

        for j in t:
            if j in tHashMap:
                tHashMap[j] += 1
            else:
                tHashMap[j] = 1

        if sHashMap == tHashMap:
            return True
        else:
            return False       