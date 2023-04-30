name = input("enter your name :")
family = input("enter your family :")

Math = int(input("enter Math Score :"))
Physics = int(input("enter Physics Score :"))
Chemistry = int(input("enter Chemistry Score :"))

avrage = (Math+Physics+Chemistry)/3

if avrage>=18:
    print("Great")
elif 12<=avrage<17:
    print("Normal")
else:
    print("fail")
