class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        for i, num in enumerate(nums):
            dict_num[num] = i
        for i, num in enumerate(nums):
            complement = target - int(num)
            if complement in dict_num.keys() and dict_num[complement] != i:
                result = list()
                result.append(i)
                result.append(dict_num[complement])
                return result
        return []
