class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            next=target-nums[i]
            if next in d and d[next]!=i:
                return sorted([d[target-nums[i]],i])
            d[nums[i]]=i