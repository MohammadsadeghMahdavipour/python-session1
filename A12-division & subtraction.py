class Math:
    def __init__(self, s , m):
        self.soorat = s
        self.makhraj = m

    def show(self):
        print(self.soorat , "/" , self.makhraj)

    def sub(self , f):
        result = Math(None , None)
        result.soorat = (self.soorat * f.makhraj) - (self.makhraj * f.soorat)
        result.makhraj = self.makhraj * f.makhraj
        return result
    
    def div(self, f):
        result = Math(None , None)
        result.soorat = self.soorat * f.makhraj
        result.makhraj = self.makhraj * f.soorat
        return result
        
f1 = Math(1 ,4)
f2 = Math(5, 4)

f1.show()
f2.show()
        
m = f1.div(f2)
n =f1.sub(f2)

m.show()
n.show()