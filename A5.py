import random

pc_number = random.randint(1 , 20)

i = 0
while True:
        
    user_number = int(input("enter your number :"))
    i = i + 1
    if user_number == pc_number:
        print("barandeh shodii")
        print("Tedad talash :", i)
        break
    if user_number<pc_number:
        print("boro balatar")
        
    if user_number>pc_number:
        print("boro paeen")