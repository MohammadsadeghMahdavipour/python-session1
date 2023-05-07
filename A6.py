import random

numbers = []
n = int(input("enter list's lengh :"))

while len(numbers) < n:
    num = random.randint(1, 10000)
    if numbers.count(num) == 0:
        numbers.append(num)

print(numbers)
