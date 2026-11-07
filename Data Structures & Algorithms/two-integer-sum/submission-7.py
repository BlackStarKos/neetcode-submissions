class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for index, num in enumerate(nums):
            val = target - num
            if val in my_dict:
                return [my_dict[val],index]
            my_dict[num] = index