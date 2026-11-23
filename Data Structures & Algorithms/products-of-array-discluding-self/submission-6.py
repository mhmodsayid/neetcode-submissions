class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resR=[1]*len(nums)
        resL=[1]*len(nums)

        for i in range(1,len(nums)):
            resR[i]=resR[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            resL[i]=resL[i+1]*nums[i+1]
        
            
        return [x*y for x,y in zip(resR,resL) ]





            
            


