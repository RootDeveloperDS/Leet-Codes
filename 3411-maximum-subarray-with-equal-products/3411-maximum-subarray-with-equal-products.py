import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(nums):
            return math.gcd(*nums)
        def lcm(nums):
            return math.lcm(*nums)
        '''def prod(nums):
            return math.prod(arr)
            prod=1
            for num in nums:
                prod=prod*num
            return prod'''
        ans=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):

                arr = nums[i:j+1]
                if math.prod(arr) == lcm(arr) * gcd(arr):
                    ans = max(ans , len(arr))

        return ans
