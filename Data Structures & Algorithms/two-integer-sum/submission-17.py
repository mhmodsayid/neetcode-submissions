class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i in range(len(nums)):
            missNum = target - nums[i]
            if missNum in hMap:
                return [hMap[missNum],i]
            else:
                hMap[nums[i]]=i
    


        