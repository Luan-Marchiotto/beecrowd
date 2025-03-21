while True:
    num = int(input())
    if num == 0:
        exit()
    print(" ".join(map(str, range(1, num + 1))))