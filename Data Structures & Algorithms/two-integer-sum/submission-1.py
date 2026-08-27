class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        other_index = 0
        ret_arr = []
        for i in range(len(nums)):
            seen[nums[i]] = i
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen.keys():
                other_index = seen[difference]
                if other_index != i:
                    ret_arr.append(other_index)
                    ret_arr.append(i)
                    break
        return sorted(list(dict.fromkeys(ret_arr)))