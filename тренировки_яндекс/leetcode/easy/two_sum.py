class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for index, current in enumerate(nums):
            tp = target - current

            if tp in dct:
                return [dct[tp], index]
            
            dct[current] = index