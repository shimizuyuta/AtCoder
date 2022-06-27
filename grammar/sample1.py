##mutable immutable

# intはimmutableになるため参照されるメモリが異なる
num1 = 10
print(id(num1))

num2 = num1

print(id(num2))

num1 += 100
print(id(num1))

print('num1',num1)
print('num2',num2)
