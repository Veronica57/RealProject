import add
import mul

print("Enter two integers")
a = int(input())
b = int(input())
print("You entered two numbers: a = ", a, ", b = ", b)
print("Choose the operation:")
print("1.Addition")
print("2.Multiplication")
c = int(input())
if (c == 1):
    print(add.add(a, b))
elif (c == 2):
    print(mul.mul(a, b))
