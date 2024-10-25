import math
while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break
    else:
        volume = (a * b * c)

        cubo = math.floor(volume ** (1/3))

        print(int(cubo))