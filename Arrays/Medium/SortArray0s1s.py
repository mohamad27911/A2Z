class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i1=0
        i2=len(nums)-1
        i=0
        while i <= i2:
            if nums[i] == 2:
                nums[i],nums[i2]=nums[i2],nums[i]
                i2-=1
            elif nums[i] ==0:
                nums[i],nums[i1]=nums[i1],nums[i]
                i1+=1
                i+=1
            else:
                i+=1
        