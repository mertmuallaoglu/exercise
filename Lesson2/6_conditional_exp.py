num = 10
isEven = ""
if num % 2 == 0:
    isEven = "Even"
else:
    isEven = "Odd"


print(isEven)
isEven = "Even" if num % 2 == 0 else "Odd"
isEven = 1 if num % 2 == 0 else -1
print(isEven)
isEven = True if num % 2 == 0 else False
isEven = num % 2 == 0

print(isEven)