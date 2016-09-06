print("This program find the greatest common divisor of two values")

m, n = eval(input("Enter two integers separated by a comma: "))

while m != 0:
    n, m = m, n%m

print(n)
