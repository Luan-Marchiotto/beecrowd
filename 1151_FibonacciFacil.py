def fibonacci_loop(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b 

n = int(input())
for i in range(n):
    print(i,fibonacci_loop(n))
