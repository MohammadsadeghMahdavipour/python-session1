def fibo(n):

    a = 1
    b = 1
    i = 1
    for i in range(0,n):
        if (a==1 & b==1 ):
            print(a)
            print(b)
        c = a + b
        print(int(c))
        a = b
        b = c




n = int(input("enter number :"))
fibo(n)


