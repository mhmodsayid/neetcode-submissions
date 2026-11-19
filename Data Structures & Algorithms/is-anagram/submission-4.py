class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash={}
        for a,b in zip(s,t):
            hash[a]=hash.get(a,0)+1
            hash[b]=hash.get(b,0)-1
        return not any(hash.values())


