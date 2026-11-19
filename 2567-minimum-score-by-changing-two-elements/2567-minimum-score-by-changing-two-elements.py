class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        #sort array
        nums.sort()
        print(nums)
        # fond and choose the min diff
        leng=len(nums)
        # since we can alwsys minimise the low score,by setting the 2 values to same numbers, and making the differernce to 0.
        # main goal is to minimise the max high score, 
        calc1= nums[leng-1]-nums[2]
        calc2= nums[leng-2]-nums[1]
        calc3= nums[leng-3]-nums[0]

        
        return min(calc1,calc2,calc3)
        