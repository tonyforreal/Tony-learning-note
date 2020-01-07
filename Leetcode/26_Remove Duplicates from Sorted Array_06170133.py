class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        for idx in range(len(nums)-1, 0, -1):
            if nums[idx] == nums[idx-1]:
                del nums[idx]
        return len(nums)
