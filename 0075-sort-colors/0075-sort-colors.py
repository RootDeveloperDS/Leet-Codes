class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Instead of sorting by comparing numbers, think of partitioning the array into four zones in a single pass using three pointers (low, mid, high):

            Confirmed 0s (Red): Everything before low
            Confirmed 1s (White): Everything from low up to mid
            Unexplored: Everything from mid through high
            Confirmed 2s (Blue): Everything after high

        mid acts as a scout walking through the unexplored zone:

            See a 0? Throw it to the left wall (low) and expand both walls forward.
            See a 1? It already belongs in the middle, so just move the scout (mid) forward.
            See a 2? Throw it to the right wall (high) and shrink the right boundary inward.
        '''
        low=mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                #swap mid and low , and increment both low and mid
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:# mid must be 2
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1 # Do not increment mid; inspect the swapped element next

'''2: Method

A rather straight forward solution is a two-pass algorithm using counting sort.

Iterate the array counting number of 0's, 1's, and 2's.

Overwrite array with the total number of 0's, then 1's and followed by 2's.
'''