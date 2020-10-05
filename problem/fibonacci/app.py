def fib(n):
    result = []

    if n == 0 or n == 1:
        return n

    result.append(0)
    result.append(1)

    for i in range(2, n+1):
        result.append(result[i-1] + result[i-2])

    return result[n]
