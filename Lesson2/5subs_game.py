import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

if num1 < num2:
    t = num1
    num1 = num2
    num2 = t
    #num1, num2 = num2, num1
3

answer: int = int(input(str(num1) + " - " + str(num2) + " = ?"))

if num1 - num2 == answer:
    print("correct")
else:
    print("wrong")