class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        the_hash = {}
        for num in nums:
            if num in the_hash:
                return True
            else:
                the_hash[num] = num
        return False