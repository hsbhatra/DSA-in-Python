def sumNNaturalNumbers(n):
    if n > 1:
        return n + sumNNaturalNumbers(n-1)
    else:
        return 1
    
print(sumNNaturalNumbers(30))
print(sumNNaturalNumbers(35))
print(sumNNaturalNumbers(40))