class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1=set()
        for i in range(0,len(nums)):
            set1.add(nums[i])
        
        if len(set1) == len(nums):
            return False
        else:
            return True
          