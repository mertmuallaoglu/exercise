"""
while logical_exp :
    stmt1
    stmt

print("while in disi")
"""
"""
i = 1
print(i)
i += 1 # i = i + 1
print(i)
i += 1 # i = i + 1
print(i)
i += 1 # i = i + 1
print(i)
"""
"""
i = 1
while i <= 10:
    print(i)
    i = i + 1


i = 0
while i <= 10:
    print(i)
    i = i + 2
    
    
i = 1
while i <= 10:
    if i % 2 == 0 :
        print(i)
    i = i + 1
"""

i = 0
sum = 0
while i < 10:
    sum += i
    print(sum, i)
    i += 1

print("sum is ", sum)



val = int(input("Enter a val 0 to terminate"))
sum = 0
while val != 0:
    sum = sum + val
    #print(sum)
    val = int(input("Enter a val 0 to terminate"))


print("sum is", sum)



