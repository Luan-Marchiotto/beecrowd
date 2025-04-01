pos = int(input())

if pos == 1:
    print("Top 1")
elif pos <= 3:
    print("Top 3")
elif pos <= 5:
    print("Top 5")
elif pos <= 10:
    print("Top 10")
elif pos <= 25:
    print("Top 25")
elif pos <= 50:
    print("Top 50")
elif pos <= 100:
    print("Top 100")