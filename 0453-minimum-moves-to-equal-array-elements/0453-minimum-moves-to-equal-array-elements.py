class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini = min(nums)
        count=0
        for i in range(len(nums)):
            diff = nums[i]- mini
            count+=diff

        return count
