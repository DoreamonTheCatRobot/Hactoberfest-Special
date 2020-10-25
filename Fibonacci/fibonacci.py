def fibonacci_good(n, computed={0:0, 1:1}): 
    if n not in computed:
        computed[n] = fibonacci_good(n-1, computed) + fibonacci_good(n-2, computed)
    return computed[n]

print(fibonacci_good(9))
