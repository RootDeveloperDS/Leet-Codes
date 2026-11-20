class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        ans=0


        # using the MEdian of the array.
        nums.sort()
        mid = nums[len(nums)//2]
        for num in nums:
            ans = ans + abs(mid-num)


        
        return ans
