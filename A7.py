def jadval():

    M = int(input("Enter the number of rows: "))
    N = int(input("Enter the number of columns: "))
        
    for i in range(M):
        for j in range(N):
            if (i + j) % 2 == 0:
                print("#", end=' ')
            else:
                print("*", end=' ')
        print()


jadval()