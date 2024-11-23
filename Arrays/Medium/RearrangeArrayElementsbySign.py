class Solution(object):
    def rearrangeArray(self, nums):
        n  = len(nums)/2
        pos=[]
        neg=[]
        for num in nums:
            if num>0:
                pos.append(num)
            else: neg.append(num)
        i = 0
        j = 0 
        ans = []
        while(n>0):
            ans.append(pos[i])
            i+=1
            ans.append(neg[j])
            j+=1
            n-=1
        return ans