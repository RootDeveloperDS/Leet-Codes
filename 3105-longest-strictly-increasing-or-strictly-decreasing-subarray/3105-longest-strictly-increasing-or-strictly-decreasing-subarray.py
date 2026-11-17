class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        incs = 1
        desc = 1
        maxx = 1

        start = end = 0

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                incs += 1
                desc = 1
            elif nums[i] > nums[i + 1]:
                desc += 1
                incs = 1
            else:  # must be equals
                incs = desc = 1

            # always save the max val
            print(incs,desc,1)
            maxx = max(incs,desc,maxx)
        
        return maxx

