class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbersSet = set(nums)
        longestConsecutive = 0

        for numbers in nums:
            if (numbers - 1) not in numbersSet:
                length = 0
                while (numbers + length) in numbersSet:
                    length += 1
                longestConsecutive = max(length, longestConsecutive)
        return longestConsecutive