import math

n = float(input())

fibo = ((pow(((1 + math.sqrt(5)) / 2),n)) - (pow(((1 - math.sqrt(5)) / 2),n))) / math.sqrt(5)

print(f"{fibo:.1f}")