class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        def check(i,j,d):
            if abs(arr1[i] - arr2[j])> d: return True
        
        count=0
        for i in range(len(arr1)):
            count+=1
            for j in range(len(arr2)):
                if not check(i,j,d):
                    count-=1
                    break
            
        return count


