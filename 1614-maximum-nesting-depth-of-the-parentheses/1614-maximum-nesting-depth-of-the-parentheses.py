class Solution:
    def maxDepth(self, s: str) -> int:
        depth=maxdepth=0
        for char in s:
            if char=='(':
                depth+=1
            elif char==')':
                depth-=1
            else:
                pass

            maxdepth=max(maxdepth,depth)
        return maxdepth
            
                