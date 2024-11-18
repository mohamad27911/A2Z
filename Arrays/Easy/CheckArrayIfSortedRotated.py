class Solution(object):
    def check(self, nums):
        if(sorted(nums)==nums):
            return True
        m = nums[0]
        for i in range(0,len(nums)-1):
            m = min(m, nums[i])
            if(nums[i]>nums[i+1]):
                if(nums[len(nums)-1]>m):return False
                for j in range(i+1,len(nums)-1):
                    if(nums[j+1]>m or nums[j+1]<nums[j] ):
                        return False            
        return True
