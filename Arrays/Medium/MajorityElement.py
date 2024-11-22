class Solution(object):
    def majorityElement(self, nums):
        map={}
        m=0
        el=0
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i],0)+1
        for key,value in map.items():
             if value >m:
                 m=value
                 el = key
        return el