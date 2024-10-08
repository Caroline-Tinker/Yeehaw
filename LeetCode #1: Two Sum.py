from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       numsMap = {}
       n = len(nums)
       
       for i in range(0,n):
            pair = target - nums[i]
            if pair in numsMap:
                return [numsMap[pair], i]
            numsMap[nums[i]] = i
