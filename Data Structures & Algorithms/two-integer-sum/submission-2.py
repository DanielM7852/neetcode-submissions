class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ret_arr = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                ret_arr.append(min(i,seen[difference]))
                ret_arr.append(max(i,seen[difference]))
            else:
                seen[nums[i]] = i
        
        return ret_arr