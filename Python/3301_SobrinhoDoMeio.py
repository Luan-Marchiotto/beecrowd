a = list(map(int, input().split()))

h, z, l = a[0], a[1], a[2]

if (h < z < l) or (l < z < h):
    print("zezinho")
elif (z < h < l) or (l < h < z):
    print("huguinho")
else:
    print("luisinho")
