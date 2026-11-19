class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = dict()
        frequency = [[] for i in range(len(nums) + 1)]

        for number in nums:
            occurence[number] = 1 + occurence.get(number,0)
        for number, cnt in occurence.items():
            frequency[cnt].append(number)
        result = []
        for i in range(len(frequency) -1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result
