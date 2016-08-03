class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        has = [0] * (len(nums) + 1)
        
        for num in nums:
            has[num] = 1
            
        for i,ha in enumerate(has):
            if ha == 0:
                return i
