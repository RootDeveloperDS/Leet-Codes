class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        smallers=[]
        largest=[]
        piv_count=0

        for i in range(len(nums)):
            if nums[i]<pivot:
                smallers.append(nums[i])
            
            elif nums[i]==pivot:
                piv_count+=1
            else:#must be x>pivot
                largest.append(nums[i])

        return smallers + [pivot]*piv_count + largest
