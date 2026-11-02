class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1=set()
        for i in range(0,len(nums)):
            if nums[i] not in set1:
                set1.add(nums[i])
        
        return len(set1) != len(nums)
    
          