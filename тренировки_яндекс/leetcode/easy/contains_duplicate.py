class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dct = {}

        for current in nums:
            if dct.get(current):
                return True
            else:
                dct[current] = 1
        return False