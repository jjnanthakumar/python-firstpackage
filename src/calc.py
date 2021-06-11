from functools import reduce
class Calculator:
    """Pass data as seperate arguments"""
    def __init__(self, *args):
        self.data = args
    
    def add(self):
        return sum(self.data)

    def sub(self):
        return reduce(lambda a,b:a-b, self.data)
    
    def mul(self):
        return reduce(lambda a,b:a*b, self.data)
    
    def div(self):
        return reduce(lambda a,b:a/(b or 1), self.data)

    def xor(self):
        return reduce(lambda a,b:a^b, self.data)
        
        
