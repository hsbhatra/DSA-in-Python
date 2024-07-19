def power(x, n):
    if n != 0:
        return x * power(x, n-1)
    else:
        return 1
    
# Example usage
x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))

result = power(x, n)
print(f"{x} raised to the power {n} is {result}")

# print(power(2, 5))
# print(power(2, 6))
# print(power(2, 7))