joias = []

while True:
    try:
        x = str(input())
        joias.append(x)
        
    except EOFError:
        break

joias = set(joias)
print(len(joias))