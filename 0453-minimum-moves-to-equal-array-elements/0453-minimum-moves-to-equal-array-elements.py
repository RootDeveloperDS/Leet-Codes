class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        mini = nums[0]
        count=0
        for i in range(1, len(nums)):
            diff = nums[i]- mini
            count+=diff

        return count
