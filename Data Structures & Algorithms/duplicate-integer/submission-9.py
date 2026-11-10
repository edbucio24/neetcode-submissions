class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set();

        for numbers in nums:
            if numbers in seen:
                return True
            seen.add(numbers)
        return False