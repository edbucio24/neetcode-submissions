class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        preFix = 1
        for number in range(len(nums)):
            result[number] = preFix
            preFix *= nums[number]
        postFix = 1
        for number in range(len(nums)-1,-1,-1):
            result[number] *= postFix
            postFix *= nums[number]
        return result


