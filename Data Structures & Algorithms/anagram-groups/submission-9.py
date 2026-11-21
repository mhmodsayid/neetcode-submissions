class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashM= {}
        def getCountArray(element:str) -> List[int]:
            count = [0]*26
            for s in element:
                for c in s:
                    index = ord(c) - ord('a')
                    count[index]+=1

            return count
        for s in strs:
            hashM.setdefault(tuple(getCountArray(s)),[]).append(s)
        return list(hashM.values())
            





