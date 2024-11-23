class Solution(object):
    def longestConsecutive(self, nums):
        map ={}
        n = sorted(nums)
        for i in range(len(n)):
            if((n[i]-1 )in map):
                map[n[i]] = map.get(n[i]-1,0)+1
            else:
                map[n[i]]=1
        m=0
        for key,value in map.items():
            m = max(m,value)
        return m
        