import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                arr = nums[i:j+1] # creates every possible array... and check its conpatibility
                if math.prod(arr) == math.lcm(*arr) * math.gcd(*arr):
                    ans = max(ans , len(arr))

        return ans
