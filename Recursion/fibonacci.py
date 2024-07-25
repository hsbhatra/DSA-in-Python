def fibonacci(n):
    fibonacci_series = []
    if n <=1:
        fibonacci_series.insert(0, n)
        return fibonacci_series
    else:
        fibonacci_series.insert(0, fibonacci(n-1) + fibonacci(n-2))
        return fibonacci_series

print(fibonacci(5))
    

