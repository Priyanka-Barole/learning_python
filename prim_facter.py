# Que-write a python program create function fact append to list.
# solution-
def fact(n):
    factor = []
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factor.append(i)

    if n > 1:
        factor.append(n)

    return factor

# Example
number = int(input("enter number:"))
result = fact(number)
print(result)

