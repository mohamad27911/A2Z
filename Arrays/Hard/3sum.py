class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        ans=[]
        
        for i in range(n):
            if nums[i] > 0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            lo,hi = i+1, n-1
            while lo < hi:
                sum = nums[i]+nums[lo]+nums[hi]
                if sum >0:
                    hi-=1
                elif sum < 0:
                    lo+=1
                else:
                    ans.append([nums[i],nums[lo],nums[hi]])
                    lo=lo+1
                    hi=hi-1
                    while lo < hi and nums[lo]==nums[lo-1]:lo+=1
                    while lo < hi and nums[hi]==nums[hi+1]:hi-=1
        return ans
        