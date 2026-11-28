class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        def heapify(heap_size, root):
            largest = root  # assume root as largest
            left = 2 * root + 1  # left node and right node
            right: int = 2 * root + 2

            # update the lergest variable with actual largest
            if (left < heap_size and nums[left] > nums[largest]):  # left inside the size, and larger
                largest = left
            if (right < heap_size and nums[right] > nums[largest]):  # right inside the size, and larger
                largest = right

            if largest != root:  # if largest is different from out assumed largest,SWAP
                nums[root], nums[largest] = nums[largest], nums[root]
                heapify(heap_size, largest)  # parent further down the subtree to restore the Max-H

        # Phase 1: Build a Max-Heap bottom-up
        for i in range(n // 2, -1, -1):  # loop from n//2 to 0 parent to adjust heap.
            heapify(n, i)

        # Phase 2: Extract elements one by one from the heap
        # go from length to 0.
        for end in range(n - 1, 0, -1):
            # swap the 0(max) value to the end (sorted location).
            nums[0], nums[end] = nums[end], nums[0]
            # fix the new root(0) in heap, after our swapping 
            heapify(end, 0)

        return nums


"""
# QUICK SORT (TLE Errored here)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def quick_sort(low, high):
            if low < high:
                p = partition(low, high)
                quick_sort(low, p - 1)
                quick_sort(p + 1, high)

        def partition(low, high):
            l = low
            h = high
            key = nums[low]  # deposit safe
            while l <= h:
                while l <= h and nums[l] <= key:
                    l += 1
                while nums[h] > key:
                    h -= 1
                # swap l and h, if needed
                if l < h:
                    nums[l], nums[h] = nums[h], nums[l]

            nums[low] = nums[h]
            nums[h] = key

            return h

        quick_sort(0, len(nums) - 1)
        return nums
"""
