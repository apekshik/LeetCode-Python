class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] 
        return max(self.helper(nums[1:]), self.helper(nums[:-1])) 

    def helper(self, nums): 
        # very important to NOT initialize these two to the first two elements of nums. 
        # think hard about the WHY. 
        rob1, rob2 = 0, 0
         
        for i in range(len(nums)):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2 
            rob2 = temp 
        
        return rob2 