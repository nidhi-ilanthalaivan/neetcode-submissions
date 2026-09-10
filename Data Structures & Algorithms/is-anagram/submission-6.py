class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS = {}
        hashT = {}
        for i in s:
            if i in hashS:
                hashS[i] += 1
            else:
                hashS[i] = 1
        
        for j in t:
            if j in hashT:
                hashT[j] += 1
            else:
                hashT[j] = 1
        
        if hashT == hashS:
            return True
        else:
            return False
        