import math

while True:

    

    num1 = int(input("enter num1 :"))

    op = input("(+ , - ,* , / , sin , cos , tan , cot , radical , factorial :) or exit :")

    if op == "sin":
        print(math.sin(num1))
        continue
             

    if op == "cos":
        print(math.cos(num1))
        continue

    if op == "radical":
        print(math.sqrt(num1))
        continue

    if op == "cot":
        print(math.cot(num1))
        continue

    if op == "tan":
        print(math.tan(num1))
        continue

    if op == "factorial":
        if num1 >= 1:
            print(math.factorial(num1))
            continue
        else:
            print("Try again")
            continue


    num2 = int(input("enter num2 :"))
    
    if op == "+":
        result = num1 + num2

    if op == "-":
        result = num1 - num2

    if op == "*":
        result = num1 * num2

    if op == "/":
        if num2 == 0:
            result = "error"
        else:
            result = num1 / num2
    if op == "exit":
        break

    print("result" , result)
