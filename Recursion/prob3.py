# Given a decimal number as input, we need to write a program to convert the given decimal number into an equivalent binary number.

# Ex:-
# Input: 7
# Output: 111

# Input: 10
# Output: 1010

def decimalToBinary(num):
    if num == 0:
        return 0
    
    return num%2 + 10 * decimalToBinary(num//2)

ans = decimalToBinary(10)
print(ans)


    
