number = int(input('Give me a value:'))
#586
digit1 = number % 10
#print(digit1)
number = number // 10
#print(number)
digit2 = number % 10
#print(digit2)
number = number // 10
print('Sum of digits are', number + digit1 + digit2)