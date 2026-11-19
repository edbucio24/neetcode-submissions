class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = dict()

        for index,value in enumerate(nums):
            difference = target - value
            if difference in prev:
                return [prev[difference],index]
            prev[value] = index

