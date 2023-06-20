class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            num_copy = nums[:]
            index = num_copy.index(num)
            num2 = num_copy.pop(index)
            num_copy = [number + num2 for number in num_copy]
            if target in num_copy:
                index2 = num_copy.index(target)
                index2 += (1 if index2 >= index else 0)
                return [index, index2]

