class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sets = {}
        sett = {}
        for i in s:
            if i in sets:
                sets[i] += 1
            else:
                sets[i] = 0
        
        for i in t:
            if i in sett:
                sett[i] += 1
            else:
                sett[i] = 0
        
        if sett == sets:
            return True
        else:
            return False
        