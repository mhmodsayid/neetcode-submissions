class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashCount={}
        for n in nums:
            hashCount[n] = hashCount.get(n,0) + 1
        
        return sorted(hashCount,key=hashCount.get)[-k:]
        
