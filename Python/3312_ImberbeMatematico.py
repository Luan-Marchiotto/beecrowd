import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

rep = int(input())
numeros = list(map(int, input().split()))
    
primos = [num for num in numeros if is_prime(num)]
    
for prime in primos:
    print(f"{prime}! = {math.factorial(prime)}")