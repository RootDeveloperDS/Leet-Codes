class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        smallest_ans = float("inf") # infinite

        for size in range(l , r+1):# we create the windows for all size from l to r 
            #print(size, l,r)
            # here starts the subproblem, with size givinn, and find the min sum of the sub arrays.
            
            curr_sum=0
            for x in range(size):# find the sum of init window ...
                curr_sum=curr_sum + nums[x]
            #print(curr_sum,x)

            if curr_sum>0:# check if the init curr_sum is small or not
                smallest_ans = min(smallest_ans, curr_sum)

            #lets move this window now slowly.
            for tail in range(x+1, len(nums)):
                curr_sum = curr_sum + nums[tail] - nums[tail-size]
                #print(curr_sum)
                if curr_sum>0:# if curr sum is +ve so find the min...
                    smallest_ans = min(smallest_ans, curr_sum)
                print("smallest_ans",smallest_ans)

            # here starts the next loop of problem with the next Size...

        return -1 if smallest_ans == float("inf") else smallest_ans

