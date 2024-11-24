class Solution(object):
    def subarraySum(self, nums, k):
        ans = 0
        sum=0
        map={0:1}
        for num in nums:
            sum += num
            if sum - k in map:
                ans+=map[sum-k]
            map[sum] = map.get(sum,0)+1            
        return ans

