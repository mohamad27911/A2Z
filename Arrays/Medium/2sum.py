class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map ={}
        for index, element in enumerate(nums):
                map[element] = index
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in map and not ( map[curr] == i):
                return [i,map[curr]]
       