class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=len(strs)
        matchGroup=[]
        group={}
        skipStr = set()
        
        for s in strs:
            key = ''.join(sorted(s))
            group.setdefault(key, []).append(s)

        return list(group.values())



