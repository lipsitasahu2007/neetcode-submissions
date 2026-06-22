class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range (len(nums)):
            k=1
            for j in range (len(nums)):
                if j != i:
                    k*=nums[j]
            l.append(k)
        return l
                
                    
        