class ProductOfNumbers:
    
    def __init__(self):
        self.pref_prod=[1]# maintain the prefix product ,To get the product of the last $k$ numbers, divide the latest prefix product by the prefix product k steps back: prefix[-1] // prefix[-1 - k] 
        

    def add(self, num: int) -> None:
        if num==0:
            # Instead of multiplying by 0, reset self.pref_prod = [1]. That wipes out all pre-zero history, so self.pref_prod only tracks valid non-zero products after the most recent 0.
            # reset the pref ,insted of multiplying by 0 ,and making every next elem 0 later.
            self.pref_prod=[1]
        else:
            self.pref_prod.append(self.pref_prod[-1]*num)

    def getProduct(self, k: int) -> int:
        if k>= len(self.pref_prod):
            return 0# if k is greater than length ,then must be encountered by 0 in product(which reset the pref_prod),so amswers becomes 0

        else:
            #calc & return actual product now.
            return self.pref_prod[-1] // self.pref_prod[-1-k]

        

        
            



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)