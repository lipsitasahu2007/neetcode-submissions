class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        c=0
        for i in nums:
            d[i]=c
            c+=1
        for i in range(len(nums)):
            next=target-nums[i]
            if next in d and d[next]!=i:
                return sorted([d[target-nums[i]],i])