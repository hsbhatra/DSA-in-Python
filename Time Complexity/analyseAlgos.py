# SUM OF N NATURAL NUMBERS

def calculateSum_1(n):
    return n*(n+1)/2

# This function's time complexity will be equal irrespectively of the value of "n".

print(calculateSum_1(3))        # 3*(3+1)/2 = (3*4)/2 = 12/2 = 6

def calculateSum_2(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

print(calculateSum_2(3))        # sum=0  ->  sum+i  ->  0+1=1  ->  1+2=3  ->  3+3=6

def calculateSum_3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum += 1

    return sum

print(calculateSum_3(3))        # sum=0  ->  0+(1)+(1+1)+(1+1+1) = 6




