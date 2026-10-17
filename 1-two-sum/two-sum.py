class Solution(object):
    def twoSum(self, nums, target):
        t = {}
        for i, n in enumerate(nums):
            if target - n in t:
                return i, t[target - n]
            t[n] = i

        
        