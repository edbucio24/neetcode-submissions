class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ourMap = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in ourMap:
                return [ourMap[difference], index]
            ourMap[value]= index
