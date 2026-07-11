class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sStore = {}
        tStore = {}

        for i in s:
            if i in sStore:
                sStore[i] += 1
            else:
                sStore[i] = 1
        
        for k in t:
            if k in tStore:
                tStore[k] += 1
            else:
                tStore[k] = 1
        
        return sStore == tStore
        