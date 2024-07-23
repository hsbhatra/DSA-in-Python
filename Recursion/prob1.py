# Given an integer n, return true if it is a power of three. Otherwise, return false.

def isPowerOfThree(n):          # Let n=9
    if n == 1:                  # n=9 != 1
        return True
    
    if n == 0 or n%3 != 0:
        return False
    
    return isPowerOfThree(n/3)


print(isPowerOfThree(9))
print(isPowerOfThree(20))