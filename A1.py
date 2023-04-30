a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter Third number :"))

f=a+b
g=b+c
h=a+c

if (a<g):
        if(b<h):
                if(c<f):
                    print("It is possible to draw a triangle")
                else:
                    print("It is not possible to draw a triangle")
        else:
            print("It is not possible to draw a triangle")
else:
            print("It is not possible to draw a triangle")


