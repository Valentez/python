a = int(input("Please, input number: "))
m = a % 10
print(m)
a = a//10
print(a)
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a//10
print(m)
