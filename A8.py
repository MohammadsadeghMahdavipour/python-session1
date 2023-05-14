import math

def solve():


    a = int(input("enter number a :"))
    b = int(input("enter number b :"))
    c = int(input("enter number c :"))
    

   
    delta = (b*b) - (4*a*c)
    if delta > 0:
        
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("2 rishe darim :", x1 , x2)
        
    elif delta == 0:
        
        x = -b / (2*a)
        print("yek rishe darim :", x)
        
    else:
        print("Moadele rishe nadarad")


solve()