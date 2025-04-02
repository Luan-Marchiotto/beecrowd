while True:
    try:
        a,b,c = map(int,input().split())
        
        if a != b and a != c:
            print("A")
        elif b != a and b != c:
            print("B")
        elif c != a and c != b:
            print("C")
        elif a == b == c:
            print("*")
        
    except EOFError:
        break