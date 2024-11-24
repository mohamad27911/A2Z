class Solution(object):
    def subarraySum(self, nums, k):
        ans = 0
        visited=[False]*len(nums)
        for i in range(len(nums)):
            target = k - nums[i]
            if(target in (nums) and not visited[nums.index(target)]):
                visited[nums.index(target)] = True
                ans+=1
        return ans+1
            
            
        