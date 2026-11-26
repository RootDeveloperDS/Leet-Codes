class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10 :# edge case optional
            return False
        
        to_remove=10
        alice=False # no one (alice) picked till now.
        while n>=to_remove:
            alice = not alice
            # print(alice,n,to_remove)
            n = n - to_remove # pickup
            to_remove-=1
            

            
        return alice
        
        