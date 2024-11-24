class Solution(object):
    def majorityElement(self, nums):
        map={}
        m=0
        el=0
        ans = []
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i],0)+1
        for key,value in map.items():
             if value > (len(nums)/3):
                 ans.append(key)
        return ans