class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        
        for num in nums:
            d[num] = d.get(num, 0) + 1

        for count in d.values():
            if count > 1:
                return True

        return False