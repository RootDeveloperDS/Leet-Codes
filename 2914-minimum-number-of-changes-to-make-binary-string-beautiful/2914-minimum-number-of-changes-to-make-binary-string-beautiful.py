class Solution:
    def minChanges(self, s: str) -> int:
        changes=0
        for i in range(0,len(s),2):# compare the each pairs , and increment coutn if the pair is not same.
            if s[i]!=s[i+1]:changes+=1

        return changes
            
    
        