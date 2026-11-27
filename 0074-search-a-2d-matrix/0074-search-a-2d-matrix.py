class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1

        def num_at_index(int_index):#returns num at index ,arr starting from 0 to n-1
            #print(matrix[int_index // cols] [int_index % cols])
            return matrix[int_index // cols] [int_index % cols]

        # apply binary search.
        while low <= high:
            mid = (low + high) // 2
            #print(mid)
        
            val = num_at_index(mid)
            if val == target:
                return True
            elif val > target:
                high = mid - 1
            else:
                low = mid + 1

        return False


